from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from patient.forms import CreateUser
from .models import Patient,Doctor
from django.contrib.auth.decorators import login_required
from .forms import DoctorProfileForm

# from django.shortcuts import render, redirect
# from .models import Doctor
# from patient.models import Patient
# from django.contrib.auth.models import User




# -------------------------------  authentication section starts :


def drLog(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pass1 = request.POST.get('password')
        try:
            Auser = User.objects.get(username=uname)
        except User.DoesNotExist:
            # Handle the case where the user does not exist
            return render(request, 'doctor/login.html', {'msg': 'User not found'})

        Auser = authenticate(request , username = uname , password = pass1)
        if Auser is not None:
            login(request, Auser)
            return redirect('useraccount')
            # return redirect('home')
    con={

    }
    return render(request,'doctor/login.html',con)


def drRegister(request):
    # form = UserCreationForm()
    count = 1
    also_doctor = 1
    form = CreateUser()
    if request.method == "POST":
        form = CreateUser(request.POST) #make all one by one loke username email pass etc so that we can access
        uname = request.POST.get('username')
        # pass1 = request.POST.get('password')
        
        if form.is_valid():
            form.save()
            try:
                obj = User.objects.get(username = uname)
                Patient.objects.create(user=obj).save()
            except User.DoesNotExist:
                return render(request, 'doctor/register.html', {'msg': 'User not found'})
            # print(obj)
            login(request,obj)
            is_staff = True
            count = 0
            # redirect to account creation of patient tp add other info
            return redirect('drAccount')

    con={
        'form':form,
    }
    return render(request,'doctor/register.html',con)


# def drAccount(request):
#     count = 0
#     obj = User.objects.get(username = request.user)
#     profile = Patient.objects.get(user = obj.id)

#     if request.method == 'POST':
#             # Update the profile fields as needed
#             # obj.email = request.POST.get('email')

# # more fields will be added

#             profile.phone = request.POST.get('phone') 
#             profile.state = request.POST.get('state')
#             profile.city = request.POST.get('city')
#             profile.pincode = request.POST.get('pincode')
#             profile.area = request.POST.get('area')
#             profile.dob = request.POST.get('dob')
#             profile.save()
#             return redirect('home')
#     con = {
#         'profile':profile,
#     }
#     return render(request,'doctor/account.html',con)


@login_required
def drAccount(request):
    try:
        user_obj = User.objects.get(username=request.user)
        doctor_profile = Doctor.objects.get(user=user_obj.id)
    except Doctor.DoesNotExist:
        # Create a new doctor profile if it doesn't exist
        doctor_profile = Doctor(user=user_obj)

    if request.method == 'POST':
        form = DoctorProfileForm(request.POST, request.FILES, instance=doctor_profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DoctorProfileForm(instance=doctor_profile)

    context = {
        'form': form,
    }

    return render(request, 'doctor/account.html', context)


# -------------------------------  authentication section ends :


def doctorSearch(request):
    city = request.POST.get('patient_location')
    specilization = request.POST.get('specialization')
    result_doctors = Doctor.objects.filter(clinic_location = city , spec = specilization)
    conc = {
        'docs' : result_doctors,
    }
    return render(request, 'doctor/result_doctor.html',conc)