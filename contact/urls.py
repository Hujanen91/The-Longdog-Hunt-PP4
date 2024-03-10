from . import views
from .views import contact_form
from django.urls import path

urlpatterns = [
    path('', contact_form, name='contact'),
]