from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from home.forms import ContactForm
from .models import *


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


def contactus(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['title']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['text']
            # try:
            #     send_mail(subject, message, from_email, ['admin@example.com'])
            # except BadHeaderError:
            #     return HttpResponse('Invalid header found.')
            return render(request, 'home/success.html')
    return render(request, "home/contactus.html", {'form': form,
                                                   'p': True})
