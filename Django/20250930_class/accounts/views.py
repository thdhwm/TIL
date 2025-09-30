from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm


# 회원 가입 페이지 (GET)
# 회원 가입 기능 (POST)
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # DB 저장 (저장한 유저 객체를 반환)
            auth_login(request, user)  # 자동 로그인 (세션 만들기)
            return redirect("bakeries:index")
    else:
        form = SignupForm()
    
    context = {
        'form': form,
    }

    return render(request, "accounts/signup.html", context)


# 로그인 페이지 (GET)
# 로그인 기능 (POST)
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)  # 로그인
            return redirect("bakeries:index")
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, "accounts/login.html", context)