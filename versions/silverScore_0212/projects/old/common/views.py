from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignupForm
# Create your views here.


# index == 메인페이지
def index(request):
    # care_list = CareRank.objects.order_by('-ratingDate')
    # context = {'care_list': care_list}
    return render(request, 'common/main.html')

# 회원가입
class SignUpView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'