from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError

def deco_auth(isauth):
    def mod_isauth(request):
        if 'username' in request.session.keys():
            return isauth(request)
        else:
            return HttpResponseRedirect('signin')
    return mod_isauth

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            User.objects.get(email=email)
            User.objects.get(username=username)
        except User.DoesNotExist or IntegrityError :
            messages.error(request,"This email id or username is already in use")
            return redirect('signup')
        newuser=User.objects.create_user(username,email,password)
        newuser.save()
        messages.success(request,"Your account has been create succesfully")
        return redirect('home')
    
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
            messages.success(request,"Sign In Successfully")
            return redirect('home')
            
        else:
            messages.error(request,"User does not exist")
            return redirect('signin')

    return render(request,'User/signin.html')

def signout(request):
    try:
        del request.session['username']
        del request.session['email']
        del request.session['password']
    except KeyError:
        pass
    logout(request)
    messages.success(request,"Successfully Sign Out")
    return HttpResponseRedirect('http://localhost:8000/')