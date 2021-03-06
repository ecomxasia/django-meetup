from django.shortcuts import get_list_or_404, get_object_or_404, render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils import timezone
from django.urls import reverse
from django.views import generic
from .models import ApplyUser
from django.utils import timezone

def index(request):
  return render(request, 'meetup/index.html')

class ListView(generic.ListView):
  template_name = 'meetup/list.html'
  context_object_name = 'latest_apply_list'

  def get_queryset(self):
    """Return the last twenty puvlished Apply Users."""
    return ApplyUser.objects.order_by('-apply_date')[:20]
    return ApplyUser.objects.filter(apply_date__lte=timezone.now(a)).order_by('-apply_date')[:20]

def search(request):
  return render(request, 'meetup/search.html')

def sact(request):
  eu = ApplyUser.objects.filter(mobile=request.POST['mobile'])
  if ( eu.count() == 1 ) :
    return HttpResponseRedirect(reverse('meetup:detail', args=(eu[0].id,)))
  else:
    return render(request, 'meetup/sact.html', {'msg': '등록된 회원을 찾을 수 없습니다.'})

def apply(request):
  return render(request, 'meetup/apply.html')

def save(request):
  ## 이메일과 이름으로 검색해서 동일 정보 있으면 리턴
  eu = ApplyUser.objects.filter(mobile=request.POST['mobile'])
  if ( eu.count() == 0 ) :
    ## 저장
    applyuser = ApplyUser(
      user_name	= request.POST['user_name'],
      email_address = request.POST['email_address'],
      company 	= request.POST['company'],
      mobile 	= request.POST['mobile'],
      question 	= request.POST['question'],
      apply_date 	= timezone.now()
    )
    applyuser.save()
    return HttpResponseRedirect(reverse('meetup:detail', args=(applyuser.id,)))
  else:
    return render(request, 'meetup/save.html', {'msg': '이미 등록하신 정보입니다.'})

class DetailView(generic.DetailView):
  model = ApplyUser
  template_name = 'meetup/detail.html'


