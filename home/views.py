from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect

from .models import SignUpForm  # Create your views here.


def home(request):
    return render(request, 'home/home.html')


def main(request):
    return render(request, 'home/main.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'home/signup.html', {'form': form})
