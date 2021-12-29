from django.shortcuts import render,redirect
from Home.forms import ContactForm, ReportForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages

def Home(request):
    res = render(request,'Home/index.html')
    return res

def ContactUs(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message,request.user.email,['tenthiesEducation@gmail.com'])
            except BadHeaderError:
                messages.error(request,"Invalid Subject")
                return redirect('contact-us')
            messages.success(request,"Message Send")
            return redirect('home')
    return render(request, 'Home/contact-us.html', {'form': form})

def Construction(request):
    return render(request,'Home/under-construction.html')

def Team(request):
    return render(request,'Home/team.html')

def Terms(request):
    return render(request,'Home/terms.html')

def Privacy(request):
    return render(request,"Home/privacy-policies.html")

def Report(request):
    if request.method == 'GET':
        form = ReportForm()
    else:
        form = ReportForm(request.POST)
        if form.is_valid():
            
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            device = form.cleaned_data['device']
            try:
                send_mail(subject,device+'\n'+message,request.user.email,['tenthiesEducation@gmail.com'])
            except BadHeaderError:
                messages.error(request,"Invalid Subject")
                return redirect('report')
            messages.success(request,"Reported")
            return redirect('home')
    return render(request, 'Home/report.html', {'form': form})
