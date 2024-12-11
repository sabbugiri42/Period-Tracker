from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Profile
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json


def home(request):
    return render(request, 'accounts/home.html') 

def signup(request):
    if request.method == 'GET':
        form = SignupForm()
        return render(request, 'accounts/signup.html', {'form': form})
    elif request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username = form.cleaned_data['username']).exists():
                form.add_error('username', 'Username already exists. Please choose another one.') 
                return render(request, 'accounts/signup.html', {'form':form})
            user = User.objects.create_user(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password']
            )
            Profile.objects.create(user=user, age=form.cleaned_data['age'])
            return render(request, 'accounts/signup.html', {'form': form, 'success': 'User created successfully'})
        return render(request, 'accounts/signup.html')
         

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required 
def save_period(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # Get the user's profile
        profile = Profile.objects.get(user=request.user)

        # Update the user's profile with the new start and end dates
        period_start = data['period_start']
        period_end = data['period_end']

        # Save the period start and end date to the user's profile
        profile.period_start = period_start
        profile.period_end = period_end
        profile.save()

        return JsonResponse({"message": "Period dates saved successfully."}, status = 200)
    return JsonResponse({"error": "Invalid request method."}, status = 400)
    
