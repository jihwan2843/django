from email import message
import imp
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from .models import User
from django.contrib import messages

# Create your views here.

def chpass(request):
    cp=request.POST.get('cpass')
    if check_password(cp, request.user.password):
        np=request.POST.get('npass')
        request.user.set_password(np)
        request.user.save()
        return redirect('acc:login')
    else:
        messages.error("패스워드 정보가 일치하지 않습니다.")
    return redirect('acc:update')

def update(request):
    if request.method == 'POST':
        u = request.user
        em = request.POST.get('mail')
        ec = request.POST.get('com')
        ep = request.FILES.get('pic')
        if ep:
            u.pic.delete()
            u.pic = ep
        u.email, u.comment = em, ec
        u.save()
        return redirect('acc:profile')

    return render(request, 'acc/update.html')

def create(request):
    if request.method == 'POST':
        ui = request.POST.get('ui')
        up = request.POST.get('upass')
        uc = request.POST.get('ucom')
        upi = request.FILES.get('upic')
        try:
            User.objects.create_user(username=ui,password=up,comment=uc,pic=upi)
            return redirect('acc:login')
        except:
            messages.error(request, "존재하는 아이디입니다.")
    return render(request, 'acc/create.html')

def delete(request):
    
    u = request.user
    rp = request.POST.get('rpass')
    if check_password(rp, u.password):
        u.pic.delete()
        u.delete()
        return redirect('acc:index') 
    return redirect('acc:profile')

def profile(request):
    return render(request, 'acc/profile.html')

def userlogout(request):
    logout(request)
    return redirect('acc:index')

def userlogin(request):
    if request.method == 'POST':
        un = request.POST.get('pid')
        up = request.POST.get('ppass')
        user=authenticate(username=un, password=up)
        if user:
            login(request, user)
            messages.success(request, f"{un}님 환영합니다.")
            return redirect('acc:index')
        else:
            messages.error(request, "계정정보가 일치하지 않습니다.")

    return render(request, 'acc/login.html')

def index(request):
    return render(request, 'acc/index.html')