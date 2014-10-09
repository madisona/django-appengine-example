
from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_page

from polls import views


urlpatterns = patterns('',
    url(r'^$', cache_page(60)(views.IndexView.as_view()), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)
