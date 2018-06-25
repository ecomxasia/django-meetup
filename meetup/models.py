import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class ApplyUser(models.Model):
  user_name = models.CharField(max_length=100)
  email_address = models.CharField(max_length=100)
  company = models.CharField(max_length=100)
  mobile = models.CharField(max_length=20)
  question = models.CharField(max_length=1000)
  apply_date = models.DateTimeField('date published')

  def __str__(self):
    return self.user_name

  def was_applied_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=3) <= self.apply_date <= now
  
  was_applied_recently.admin_order_field = 'apply_date'
  was_applied_recently.boolean = True
  was_applied_recently.short_description = 'Applied recently'

