
import datetime
from django import test
from django.utils import timezone

from polls import models


class QuestionModelTests(test.TestCase):

    def setUp(self):
        self.sut = models.Question

    def test_was_published_recently_when_pub_date_is_within_one_day(self):
        pub_date = datetime.datetime(2014, 1, 1)

        now_func = lambda: datetime.datetime(2014,1, 2)
        q = self.sut(pub_date=pub_date)
        self.assertEqual(True, q.was_published_recently(now_func))

    def test_was_not_published_recently_when_pub_date_is_more_than_one_day(self):
        pub_date = datetime.datetime(2014, 1, 1)

        now_func = lambda: datetime.datetime(2014, 1, 3)
        q = self.sut(pub_date=pub_date)
        self.assertEqual(False, q.was_published_recently(now_func))

    def test_was_not_published_recently_when_pub_date_is_in_future(self):
        pub_date = datetime.datetime(2014, 2, 1)

        now_func = lambda: datetime.datetime(2014, 1, 1)
        q = self.sut(pub_date=pub_date)
        self.assertEqual(False, q.was_published_recently(now_func))
