# edunest/core/views.py

from django.shortcuts import render, redirect  # 👈 Added redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'core/home.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')  # 👈 This now works because redirect is imported
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form': form})


def courses(request):
    return render(request, 'core/courses.html')

def updates(request):
    return render(request, 'core/updates.html')

@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')