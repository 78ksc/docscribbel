from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    pic = models.ImageField(upload_to='images/patient', blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    number_verified = models.BooleanField(default=False)
    state = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    area = models.CharField(max_length=200, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)

