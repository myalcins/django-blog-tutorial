from django import forms
from django.forms import fields
from blog.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('email', 'name', 'title', 'message')