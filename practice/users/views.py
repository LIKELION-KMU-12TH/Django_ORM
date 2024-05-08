from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import auth

#auth가 들어가는건 다 인증하는 것
#장고는 회원가입,로그인 등을 기능을 간단하게 제공해줌

#회원가입
def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email = request.POST['email'],
            )
            
            profile = Profile(
                user=user,
                nickname=request.POST['nickname'],
                image=request.FILES.get('profile_image'),
            )

            profile.save()
             #우리가 만든 모델은 save를 해줘야 db에 반영이됨
            auth.login(request, user)
            return redirect('home')
        
        return render(request, 'signup.html')
    return render(request, 'signup.html')

#로그인
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        return render(request, 'login.html')
    return render(request, 'login.html')

#로그아웃
def logout(request):
    auth.logout(request)
    return redirect('home')