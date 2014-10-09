
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.db.models import Sum
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from polls.models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    from google.appengine.api import taskqueue

    p = get_object_or_404(Question, pk=question_id)
    choice = request.POST.get('choice')
    if not choice:
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })

    else:
        taskqueue.add(url=reverse("polls:process-vote"),
                      params={
                          "question_id": question_id,
                          "choice": choice,
                      },
                      queue_name="processVotes")

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


@csrf_exempt
def process_vote(request):
    import time
    time.sleep(5)

    question_id = request.POST["question_id"]

    p = get_object_or_404(Question, pk=question_id)
    selected_choice = p.choice_set.get(pk=request.POST['choice'])
    selected_choice.votes += 1
    selected_choice.save()

    return HttpResponse(status=201)


@csrf_exempt
def email_summary(request):
    total_votes = Choice.objects.all().aggregate(total_votes=Sum('votes'))

    subject = 'Pyowa Summary Polling Job'
    body = 'There have been {total_votes}.'.format(**total_votes)

    send_mail(subject, body, settings.DEFAULT_FROM_EMAIL,
        ['receiver@example.com'], fail_silently=False)

    return HttpResponse(status=201)
