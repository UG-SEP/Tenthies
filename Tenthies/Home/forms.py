from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Subject',
        'type': 'text',
        }),required=True)
    
    message = forms.CharField(label='', widget=forms.Textarea(attrs={
        'placeholder': 'Start writing your message from here...',
        'type': 'text',
        'cols': 40,
        }),required=True)

class ReportForm(forms.Form):
    subject = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Title',
        'type': 'text',
        }),required=True)
    device=forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Device Name',
        'type': 'text',
        }),required=True)
    message = forms.CharField(label='', widget=forms.Textarea(attrs={
        'placeholder': 'Steps to occur the Problem',
        'type': 'text',
        'cols': 40,
        }),required=True)

