from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ContactForm


def contact_form_view(request):
    """
    The view for the contactform.
    Handels the contact form submission.
    Handels both a POST and GET request.
    The POST handles the submitting of the message,
    it makes sure it gets saved and sent to the database.
    The GET request initializes an empy contact form.
    """
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Thank you for your message. "
                                 "I will get back to you as soon as possible.")
            return HttpResponseRedirect(request.path_info)
    else:
        contact_form = ContactForm()
    return render(request, 'contact.html', {'contact_form': contact_form})
