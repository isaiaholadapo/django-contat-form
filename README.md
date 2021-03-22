# Pebblesoft contact us form

I created a contact us form with Django and Django rest framework 
## Installation

Clone this GitHub repository with the URL below.

```bash
git clone https://github.com/isaiaholadapo/django-contat-form.git
```
Install the required packages

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
## Gmail Setup

Change the following variables from settings.py

```python
EMAIL_HOST_USER= Gmail username
EMAIL_HOST_PASSWORD= Gmail password
receiver_email= Email receiver address
```

Change the following variables from contactform/views.py & contactform/api/views.py

```python

receiver_email= Email receiver address e.g. ['example@example.com']
```
## API Usage
POST request URL: http://127.0.0.1:8000/api/contacts


```python
{
    "name": "isaiah Oladapo",
    "sender": "isaiah@gmail.com",
    "message": "How can I download the app"
}
```
