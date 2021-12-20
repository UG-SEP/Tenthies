from django.http import response
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from Tenthies.settings import EMAIL_HOST_USER
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail

def deco_auth(isauth):
    def mod_isauth(request):
        if 'username' in request.session.keys():
            return isauth(request)
        else:
            return HttpResponseRedirect('http://localhost:8000/User/signin')
    return mod_isauth
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        newuser=User.objects.create_user(username,email,password)
        newuser.save()
        messages.success(request,"Your account has been create succesfully")
        return redirect('signin')
    
    return render(request,'User/signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username,email=email,password=password)
        if user is not None:
            login(request,user)
            request.session.modified = True
            request.session['username']=username
            request.session['email']=email
            request.session['password']=password
            """user.is_active=False
            email_body='Testing'
            email_subject="Test"
            email_from=EMAIL_HOST_USER
            recepient_list = ["ujjwaloffical001@gmail.com"]
            send_mail(email_subject,email_body,email_from,recepient_list)"""
            return redirect('http://localhost:8000/Profile')
            
        else:
            return redirect('http://localhost:8000/')

    return render(request,'User/signin.html')

def signout(request):
    try:
        del request.session['username']
        del request.session['email']
        del request.session['password']
    except KeyError:
        pass
    logout(request)
    return HttpResponseRedirect('http://localhost:8000/')

@deco_auth
def change_password(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        old_password = request.POST.get('oldpassword')
        new_password = request.POST.get('newpassword')
        user = authenticate(username=username,email=email,password=old_password)
        if user is not None:
            user.set_password(new_password)
            user.save()
            return redirect('http://localhost:8000/Profile')
        else:
            return redirect('http://localhost:8000/')

    return render(request,'User/change_password.html')

    
