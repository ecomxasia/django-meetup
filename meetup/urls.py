from django.urls import path

from . import views

app_name = 'meetup'
urlpatterns = [
  path('', views.index, name='index'),
  path('list/', views.list, name='list'),
  path('apply/', views.apply, name='apply'),
  path('save/', views.save, name='save'),
  path('<int:applyuser_id>/', views.detail, name='detail'),
]
