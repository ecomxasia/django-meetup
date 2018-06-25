from django.urls import path

from . import views

app_name = 'meetup'
urlpatterns = [
  path('', views.index, name='index'),
  path('save/', views.save, name='save'),
  path('apply/', views.apply, name='apply'),
  path('search/', views.search, name='search'),
  path('sact/', views.sact, name='sact'),
  path('list/', views.ListView.as_view(), name='list'),
  path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
