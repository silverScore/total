from django.contrib.auth import get_user_model, login, authenticate, logout
# from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LoginView as BaseLoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from .forms import SignupForm

# Create your views here.

User = get_user_model()

# index == mainpage
class IndexView(generic.View):
    def get(self, request):
        return render(request, 'common/index.html')

# 회원가입
class SignUpView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('common:login')
    template_name = 'common/signup.html'
    
# 로그인
class LoginView(BaseLoginView):
    template_name = 'common/login.html'
    
    def dispatch(self, request, *args, **kwargs):
        if 'care_id' in kwargs:
            request.session['care_id'] = kwargs['care_id']
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        next_url = self.request.GET.get('next', reverse_lazy('common:main'))
        care_id = self.request.session.get('care_id', None)
        if care_id:
            next_url = reverse_lazy('care_detail', kwargs={'pk': care_id})
        return next_url
