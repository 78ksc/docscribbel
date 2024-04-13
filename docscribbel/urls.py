"""docscribbel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import render,redirect
from doctor.models import Doctor,Appoint,Specilization
from django import forms
from patient.models import Patient
from django.conf import settings
from django.conf.urls.static import static


class AppointForm(forms.ModelForm):
    class Meta:
        model = Appoint
        fields = ['date_of_appointment']
        widgets = {
            'date_of_appointment': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # You can set default values for other fields here
    #     self.fields['request_created_by'].widget.attrs['readonly'] = True
    #     self.fields['alloted_doctor'].widget.attrs['readonly'] = True
    #     self.fields['prescription_pad'].widget.attrs['readonly'] = True
    #     self.fields['pacient_name'].widget.attrs['readonly'] = True
    #     self.fields['doctor_spec'].widget.attrs['readonly'] = True
    #     self.fields['pacient_addr'].widget.attrs['readonly'] = True
    #     self.fields['appointment_status'].widget.attrs['readonly'] = True



def doctorAppoint(request):
    doctor = int(request.GET.get('sdoctor'))
    appoint = request.GET.get('sappoint')
    if request.method == "POST":
        date_time = request.POST.get('date_and_time')
        try:
            doc_obj = Doctor.objects.get(id=doctor)
            print(doc_obj)
            app_obj = Appoint.objects.get(id=appoint)
            print(app_obj)
            app_obj.date_of_appointment=date_time
            app_obj.alloted_doctor=doc_obj
            app_obj.save()
        except:
            pass
        return redirect('appointment_fixed',appoint=app_obj.id)
    return render(request,'doctor/appointment_time.html')


def appointment_fixed(request,appoint):
    app_obj = Appoint.objects.get(id=appoint)
    return render(request, 'doctor/appointment_fixed.html',{'app_obj':app_obj})
    
def result_doctors(request):
    try:
        req_creater = Patient.objects.get(user=request.user)
    except:
        req_creater = None
    pname = request.GET.get('patient_name')
    city = request.GET.get('patient_location')
    specilization = request.GET.get('specialization')
    result_doctors = Doctor.objects.filter(clinic_location = city , spec = specilization)
    appointment = Appoint.objects.create(
        request_created_by=req_creater,
        pacient_name=pname,
        doctor_spec=specilization,
        pacient_addr=city,
        )
    appointment.save()
    print("appointment details : ")
    print(appointment.id)
    conc = {
        'docs' : result_doctors,
        'refrence' : appointment.id,
    }
    return render(request, 'result_doctors.html',conc)



def home(request):
    all_docs = Doctor.objects.all()
    try:
        patient = Patient.objects.get(user = request.user)
    except:
        patient=None
    
    specializations = Specilization.objects.all()
    all_app = Appoint.objects.filter(request_created_by=patient)
    con = {
        'all_docs' : all_docs,
        'all_app' : all_app,
        'specializations':specializations,
    }
    return render(request,'index.html',con)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('', include('doctor.urls')),
    path('', include('patient.urls')),
    path('result_doctors/',result_doctors,name='result_doctors'),
    path('book_appointment/', doctorAppoint, name='book_appointment'),
    path('appointment_fixed/<str:appoint>/', appointment_fixed, name='appointment_fixed')

]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
