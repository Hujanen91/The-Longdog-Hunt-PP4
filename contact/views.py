from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact_form_view(request):
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Thank you for your message. "
                                 "I will get back to you as soon as possible.")
    else:
        contact_form = ContactForm()
    return render(request, 'contact.html', {'contact_form': contact_form})
