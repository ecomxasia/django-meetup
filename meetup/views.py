from django.shortcuts import get_list_or_404, get_object_or_404, render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils import timezone
from django.urls import reverse
from .models import ApplyUser

def index(request):
  return render(request, 'meetup/index.html')

def list(request):
  latest_apply_list = ApplyUser.objects.order_by('-apply_date')[:5]
  context = { 'latest_apply_list': latest_apply_list }
  return render(request, 'meetup/list.html', context)

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

def detail(request, applyuser_id):
  applyuser = get_object_or_404(ApplyUser, pk=applyuser_id)
  return render(request, 'meetup/detail.html', {'applyuser': applyuser})


  user_name = models.CharField(max_length=100)
  email_address = models.CharField(max_length=100)
  company = models.CharField(max_length=100)
  mobile = models.CharField(max_length=20)
  question = models.CharField(max_length=1000)
  apply_date = models.DateTimeField('date published')

