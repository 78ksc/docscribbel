from django.core.management.base import BaseCommand
from doctor.models import Specilization

class Command(BaseCommand):
    help = 'Initialize specialization data in the database'

    def handle(self, *args, **options):
        specializations = [
            "General Physician",
            "Cardiologist",
            "Dermatologist",
            "Orthopedic Surgeon",
            "Pediatrician",
            "Neurologist",
            "Gastroenterologist",
            "Endocrinologist",
            "Ophthalmologist",
            "ENT Specialist",
            "Urologist",
            "Allergist/Immunologist",
            "Anesthesiologist",
            "Cardiac Electrophysiologist",
            "Colorectal Surgeon",
            "Critical Care Medicine Specialist",
            "Diagnostic Radiologist",
            "Emergency Medicine Specialist",
            "Family Medicine Physician",
            "Geneticist",
            "Geriatrician",
            "Hematologist",
            "Infectious Disease Specialist",
            "Internal Medicine Physician",
            "Medical Geneticist",
            "Nephrologist",
            "Nuclear Medicine Specialist",
            "Obstetrician/Gynecologist (OB/GYN)",
            "Occupational Medicine Specialist",
            "Oncologist",
            "Otolaryngologist (ENT)",
            "Pathologist",
            "Physiatrist",
            "Plastic Surgeon",
            "Psychiatrist",
            "Pulmonologist",
            "Radiation Oncologist",
            "Rheumatologist",
            "Sleep Medicine Specialist",
            "Sports Medicine Specialist",
            "Thoracic Surgeon",
            "Urogynecologist",
            "Vascular Surgeon",
        ]


        for spec in specializations:
            Specilization.objects.get_or_create(specs=spec)
