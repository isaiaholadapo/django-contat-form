from django.urls import path

from contactform.api.views import api_create_contact_view

app_name = 'contactform'

urlpatterns = [
    path('contacts', api_create_contact_view, name="contact-api"),
]