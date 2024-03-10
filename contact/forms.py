from .models import ContactForm
from django import forms


class contact_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')