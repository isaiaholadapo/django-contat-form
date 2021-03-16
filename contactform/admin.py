from django.contrib import admin
from contactform.models import ContactModel

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'sender', 'message']


admin.site.register(ContactModel, ContactAdmin)
