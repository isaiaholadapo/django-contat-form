from django import forms
from contactform.models import ContactModel

class CreateContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'sender', 'message']