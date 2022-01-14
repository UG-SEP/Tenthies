from django.core.mail import message, send_mail
from django.conf import settings

def send_forget_password_mail(email,token):
    subject = "Forget password"
    message = f'Click on the link to reset your password https://10thies.live/User/new-password/{token}/'
    from_email = settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message,from_email,recipient_list)