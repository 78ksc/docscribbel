from django.urls import path
from .views import *

urlpatterns = [
    path('login/', log, name='login'),
    path('logout/', logo, name='logout'),
    path('register/', register,name='register'),
    path('account/', patientAccount, name='account'),
    path('bmi/', bmi, name='bmi'),
   
]