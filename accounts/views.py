from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Signup successful! Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'Form is invalid. Please correct the errors.')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.user_type == 'doctor':
                return redirect('doctor_dashboard')
            else:
                return redirect('patient_dashboard')
    return render(request, 'accounts/login.html')

@login_required
def doctor_dashboard(request):
    return render(request, 'accounts/doctor_dashboard.html', {'user': request.user})

@login_required
def patient_dashboard(request):
    return render(request, 'accounts/patient_dashboard.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('login')

