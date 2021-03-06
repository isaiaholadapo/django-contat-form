# Generated by Django 3.1.7 on 2021-03-16 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w3lName', models.CharField(max_length=50)),
                ('w3lSender', models.EmailField(max_length=50)),
                ('w3lMessage', models.TextField(max_length=5000)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
