from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from decouple import config


from contactform.models import ContactModel
from contactform.api.serializers import ContactSerailizer

# api contact form view
@api_view(['POST', ])
def api_create_contact_view(request):
    if request.method == "POST":
        serializer = ContactSerailizer(data=request.data)
        if serializer.is_valid():
            name = request.POST['name']
            sender = request.POST['sender']
            message = request.POST['message']

            # send mail
            send_mail(
                'Contact Form mail from ' + name,
                'Sender email: ' + ' ' + sender + '\n' + message,
                sender,
                ['examplw@example.com'],
            )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
