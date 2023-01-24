from django import forms
from django.forms import ModelForm
# import your model
from .models import customer

# Create a customer form
class CustomerForm(ModelForm):
    class Meta:
        model = customer
        fields = ('firstname', 'lastname','emailaddress')

        

