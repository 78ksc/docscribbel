from django.urls import path
from .views import *
from patient.views import logo

urlpatterns = [
    path('drlogin/', drLog, name='drLogin'),
    # path('drlogout/', logo, name='logout'),
    path('drregister/', drRegister,name='drRegister'),
    path('draccount/', drAccount, name='drAccount'),

]