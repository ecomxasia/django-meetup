import datetime
from django.test import TestCase
from django.utils import timezone

from .models import ApplyUser

# Create your tests here.
class ApplyUserModelTests(TestCase):

  def test_was_applied_recently_with_future_apply(self):
    time = timezone.now() + datetime.timedelta(days=30)
    future_apply = ApplyUser(apply_date=time)
    self.assertIs(future_apply.was_applied_recently(), False)

  def test_was_applied_recently_wih_old_apply(self):
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_apply = ApplyUser(apply_date=time)
    self.assertIs(old_apply.was_applied_recently(), False)

  def test_was_applied_recently_wih_recent_apply(self):
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_apply = ApplyUser(apply_date=time)
    self.assertIs(recent_apply.was_applied_recently(), True)
