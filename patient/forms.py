from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Patient

class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name','last_name','email','username','password1','password2',
        ]

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ['user','number_verified']