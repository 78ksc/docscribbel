from django import forms
from .models import Doctor

class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = Doctor
        # fields = '__all__'
        exclude = ['user','number_verified']
