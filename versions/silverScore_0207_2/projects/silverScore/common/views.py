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


# 회원가입 페이지
class SignUpView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'common/signup.html'

# 인후님
# def signup(request):
#     if request.method == "POST":
#         user_form = UserForm(request.POST, instance=request.user)
#         signup_form = SignupForm(request.POST, instance=request.user.user_profile)
#         if user_form.is_valid() and signup_form.is_valid():
#             user_form.save()
#             signup_form.save()
#             username = user_form.cleaned_data.get('username')
#             raw_password = user_form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)   # 사용자 인증
#             login(request, user)    # 로그인
#             return redirect('index')
#     else:
#         user_form = UserForm(instance=request.user)
#         signup_form = SignupForm(instance=request.user.user_profile)

#     return render(request, 'common/signup.html', {'user_form': user_form, 'signup_form': signup_form})
