from django.contrib import admin

# Register your models here.

from .models import ApplyUser

class ApplyUserAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields': ['user_name']}), 
    (None, {'fields': ['company']}), 
    (None, {'fields': ['email_address']}), 
    (None, {'fields': ['mobile']}), 
    (None, {'fields': ['question']}), 
    ('Date information', {'fields': ['apply_date']}), 
  ]

  list_display = ( 'user_name', 'company', 'email_address', 'mobile', 'was_applied_recently' )
  list_filter = [ 'apply_date' ]
  search_fields = ['user_name', 'company', 'email_address', 'mobile' ]

admin.site.register(ApplyUser, ApplyUserAdmin)


