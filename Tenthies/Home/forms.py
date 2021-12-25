from django import forms

class ContactForm(forms.Form):
    to_email = forms.CharField(label='', widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your email',
        'type': 'email',
        }),required=True)
    
    subject = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Subject',
        'type': 'text',
        }),required=True)
    
    message = forms.CharField(label='', widget=forms.Textarea(attrs={
        'placeholder': '   Start writing your message from here...',
        'type': 'text',
        'cols': 40,
        }),required=True)

