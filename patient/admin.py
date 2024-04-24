from django.contrib import admin

# Register your models here.
# admin.py

from django.contrib import admin
from .models import Symptom, Precaution, Medication, Diet, Workout, Disease

admin.site.register(Symptom)
admin.site.register(Precaution)
admin.site.register(Medication)
admin.site.register(Diet)
admin.site.register(Workout)
admin.site.register(Disease)
