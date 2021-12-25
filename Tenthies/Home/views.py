from django.shortcuts import render,redirect
from Home.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

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
            to_email = form.cleaned_data['to_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message,'ujjwalcomputerpro1@gmail.com',[to_email])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')
    return render(request, 'Home/contact-us.html', {'form': form})

def Construction(request):
    return render(request,'Home/under-construction.html')