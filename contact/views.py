from django.shortcuts import render
from .models import About, ContactForm

# Create your views here.
def contact_form(request):
    """
    Renders the About page
    """
    contact = ContactForm.objects.all()

    return render(
        request,
        "contact.html",
        {"contact": contact_form},
    )