# Generated by Django 3.1.7 on 2021-03-16 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactform', '0002_remove_contactmodel_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmodel',
            old_name='w3lMessage',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='contactmodel',
            old_name='w3lName',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='contactmodel',
            old_name='w3lSender',
            new_name='sender',
        ),
    ]
