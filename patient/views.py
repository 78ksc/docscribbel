from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import CreateUser,PatientForm
from .models import Patient
from django.contrib.auth.decorators import login_required
from django.views import View


# -------------------------------  authentication section starts :
def log(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pass1 = request.POST.get('password')
        try:
            Auser = User.objects.get(username=uname)
        except User.DoesNotExist:
            # Handle the case where the user does not exist
            return render(request, 'patient/login.html', {'msg': 'User not found'})

        Auser = authenticate(request , username = uname , password = pass1)
        if Auser is not None:
            login(request, Auser)
            # return redirect('account')
            return redirect('home')
    con={

    }
    return render(request,'patient/login.html',con)


# def register(request):
#     form = CreateUser()
    
#     if request.method == "POST":
#         form = CreateUser(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
            
#             try:
#                 user = User.objects.get(username=username)
#             except User.DoesNotExist:
#                 return render(request, 'patient/register.html', {'msg': 'User not found'})
            
#             # Create patient profile
#             Patient.objects.create(user=user)
            
#             # Login the user
#             # login(request, user)
#             if user is not None:
#                 login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#                 return redirect('home')
            
#             # Redirect to account creation for patient to add other info
#             # return redirect('account')
        
#         print(form.errors)
    
#     context = {
#         'form': form,
#     }
#     return render(request, 'patient/register.html', context)

def register(request):
    form = CreateUser()
    
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return render(request, 'patient/register.html', {'msg': 'User not found'})
            
            # Create patient profile
            Patient.objects.create(user=user)
            
            # Login the user
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            
            # Redirect to account creation for patient to add other info
            return redirect('account')
        
        print(form.errors)
    
    context = {
        'form': form,
        'err':form.errors,
    }
    return render(request, 'patient/register.html', context)
def logo(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    return render(request,'patient/logout.html')


# def patientAccount(request):
#     count = 0
#     obj = User.objects.get(username = request.user)
#     profile = Patient.objects.get(user = obj.id)

#     if request.method == 'POST':
#             # Update the profile fields as needed
#             # obj.email = request.POST.get('email')
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
#     return render(request,'patient/account.html',con)

@login_required
def patientAccount(request):
    try:
        user_obj = User.objects.get(username=request.user)
        patient_profile = Patient.objects.get(user=user_obj.id)
    except Patient.DoesNotExist:
        patient_profile = Patient(user=user_obj)
    if request.method == 'POST':
        form = PatientForm(request.POST,request.FILES,instance=patient_profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PatientForm(instance=patient_profile)
    context = {
        'form': form,
    }
    return render(request, 'patient/account.html', context)



# def drAccount(request):
#     try:
#         user_obj = User.objects.get(username=request.user)
#         doctor_profile = Doctor.objects.get(user=user_obj.id)
#     except Doctor.DoesNotExist:
#         # Create a new doctor profile if it doesn't exist
#         doctor_profile = Doctor(user=user_obj)

#     if request.method == 'POST':
#         form = DoctorProfileForm(request.POST, request.FILES, instance=doctor_profile)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = DoctorProfileForm(instance=doctor_profile)

#     context = {
#         'form': form,
#     }

#     return render(request, 'doctor/account.html', context)


# -------------------------------  authentication section ends :


def bmi(request):
    return render(request,'patient/bmi.html')