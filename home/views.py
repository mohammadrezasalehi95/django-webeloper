from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
    return render(request, 'home/home.html')


def main(request):
    return render(request, 'home/main.html')


def signup(request):
    return render(request, 'home/signup.html')
