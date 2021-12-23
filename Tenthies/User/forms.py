# forms.py

from django import forms
from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm

class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'placeholder': 'Email Address',
        'type': 'email',
        }))

class UserPasswordResetConfirmForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetConfirmForm, self).__init__(*args, **kwargs)

    new_password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter New Password',
        'type': 'password',
        }))
    new_password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm New Password',
        'type': 'password',
        }))
