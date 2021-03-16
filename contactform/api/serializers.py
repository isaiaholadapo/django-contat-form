from rest_framework import serializers
from contactform.models import ContactModel

class ContactSerailizer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = ['name', 'sender', 'message']
