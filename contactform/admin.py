from django.contrib import admin
from contactform.models import ContactModel

# Contact form model.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'sender', 'message']


admin.site.register(ContactModel, ContactAdmin)
