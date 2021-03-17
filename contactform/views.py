from django.shortcuts import render, redirect
from contactform.forms import CreateContactForm
from django.core.mail import send_mail
from django.contrib import messages
from decouple import config

# Home page view
def home_view(request):
    return render(request, 'contactform/index.html', {})

# Contact page view
def contact_view(request):
    if request.method == "POST":
        form = CreateContactForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            sender = request.POST['sender']
            message = request.POST['message']

            # send mail
            send_mail(
                'Contact Form mail from ' + name,
                'Sender email: ' + ' ' + sender + '\n' + message,
                sender,
                [config('receiver_email')],
            )
            form.save()
            messages.success(
                request, 'Thank you for contacting us, we will get back to you shortly...')
            return redirect('contact')
    else:
        return render(request, 'contactform/contact.html', {})
