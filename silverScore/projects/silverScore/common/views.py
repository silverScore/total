from django.contrib.auth import get_user_model, login, authenticate, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic.edit import CreateView
from .forms import SignupForm

# Create your views here.

User = get_user_model()

# index == 메인페이지
class IndexView(generic.View):
    def get(self, request):
        return render(request, 'common/index.html')
    
# def index(request):
    # care_list = CareRank.objects.order_by('-ratingDate')
    # context = {'care_list': care_list}
    # return render(request, 'common/main.html')

# 회원가입
class SignUpView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'