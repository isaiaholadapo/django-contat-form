from django.db import models

# Contact form models.
class ContactModel(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    sender = models.EmailField(max_length=50, null=False, blank=False)
    message = models.TextField(max_length=5000, null=False, blank=False)
