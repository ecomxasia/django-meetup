from django.contrib import admin

# Register your models here.

from .models import Question, Choice, ApplyUser

admin.site.register(ApplyUser)
admin.site.register(Question)
admin.site.register(Choice)


