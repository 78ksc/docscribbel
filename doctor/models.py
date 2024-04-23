from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient

class Specilization(models.Model):
    specs = models.CharField(max_length=100)

    def __str__(self):
        return self.specs

class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    pic = models.ImageField(upload_to='images/doc', blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    number_verified = models.BooleanField(default=False)
    dob = models.DateField(blank=True, null=True)
    spec = models.ForeignKey(Specilization, on_delete=models.DO_NOTHING, null=True, blank=True)
    edu = models.CharField(max_length=40)
    exp = models.IntegerField()
    consulting_fees = models.IntegerField()
    clinic_name = models.CharField(max_length=200, blank=True, null=True)
    clinic_location = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    area = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username

class PrescriptionPad(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    days = models.IntegerField()
    investigations = models.ManyToManyField('Investigation', related_name='prescription_investigations')
    prescriptions = models.ManyToManyField('Medicen', related_name='prescription_medicens')

class Appoint(models.Model):
    APPOINTMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('cancelled', 'Cancelled'),
    ]
    request_created_by = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    alloted_doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    prescription_pad = models.ForeignKey(PrescriptionPad, on_delete=models.SET_NULL, null=True)
    pacient_name = models.CharField(max_length=40)
    doctor_spec = models.CharField(max_length=120, blank=True)
    pacient_addr = models.CharField(max_length=200)
    appointment_status = models.CharField(max_length=20, choices=APPOINTMENT_STATUS_CHOICES, default='pending')
    date_of_appointment = models.DateTimeField(null=True)

class Medicen(models.Model):
    pic = models.ImageField(upload_to='images/med', blank=True, null=True)
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()

class Investigation(models.Model):
    i_name = models.CharField(max_length=200, unique=True)
    i_price = models.IntegerField()
    i_result = models.CharField(max_length=200)


class Medicensell(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/med', blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    expiry_date = models.DateField()

    def __str__(self):
        return self.name
