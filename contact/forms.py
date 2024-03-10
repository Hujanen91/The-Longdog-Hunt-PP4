from .models import ContactForm
from django import forms


class contact_form(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ('name', 'email', 'message')