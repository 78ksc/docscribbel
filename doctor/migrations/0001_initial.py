# Generated by Django 3.2.21 on 2023-11-25 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(blank=True, null=True, upload_to='images/doc')),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('number_verified', models.BooleanField(default=False)),
                ('dob', models.DateField(blank=True, null=True)),
                ('spec', models.CharField(max_length=120)),
                ('edu', models.CharField(max_length=40)),
                ('exp', models.IntegerField()),
                ('consulting_fees', models.IntegerField()),
                ('clinic_name', models.CharField(blank=True, max_length=200, null=True)),
                ('clinic_location', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('area', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Investigation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_name', models.CharField(max_length=200, unique=True)),
                ('i_price', models.IntegerField()),
                ('i_result', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Medicen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(blank=True, null=True, upload_to='images/med')),
                ('name', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PrescriptionPad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.IntegerField()),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
                ('investigations', models.ManyToManyField(related_name='prescription_investigations', to='doctor.Investigation')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
                ('prescriptions', models.ManyToManyField(related_name='prescription_medicens', to='doctor.Medicen')),
            ],
        ),
        migrations.CreateModel(
            name='Appoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_appointment', models.DateTimeField(auto_created=True)),
                ('pacient_name', models.CharField(max_length=40)),
                ('doctor_spec', models.CharField(blank=True, max_length=120)),
                ('pacient_addr', models.CharField(max_length=200)),
                ('appointment_status', models.CharField(max_length=40)),
                ('alloted_doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctor.doctor')),
                ('prescription_pad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctor.prescriptionpad')),
                ('request_created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient.patient')),
            ],
        ),
    ]
