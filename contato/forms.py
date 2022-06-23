from django.forms import ModelForm
from .models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact     
        fields = ('nome','numero','email', 'message')