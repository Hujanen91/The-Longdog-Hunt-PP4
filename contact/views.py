from django.shortcuts import render
from .models import About, ContactForm
from .forms import contact_form 

# Create your views here.
def contact_form(request):
    """
    Renders the contact page
    """
    contact = ContactForm.objects.all()

    return render(
        request,
        "contact.html",
        {"contact": contact_form,
         "contact_form": contact_form},
    )