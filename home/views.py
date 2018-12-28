from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from home.forms import ContactForm
from .forms import EditProfileForm
from .models import *
from django.conf import settings


def home(request):
    return render(request, 'home/home.html')


def main(request):
    return render(request, 'home/main.html')


def profile(request):
    user = request.user
    if user.is_authenticated:
        if not Profile.objects.all().filter(user=user).exists():
            return render(request, 'home/profile.html',
                          {'firstname': user.first_name, 'lastname': user.last_name, 'username': user.username})
        else:
            return render(request, 'home/profile.html',
                          {'firstname': user.first_name, 'lastname': user.last_name, 'username': user.username,
                           'bio': user.profile.bio, 'gender': user.profile.gender,
                           'image': user.profile.get_image().url})
    else:
        return HttpResponse("login first", status=401)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
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
            try:
                send_mail(subject, message + " " + from_email, settings.EMAIL_HOST_USER,
                          recipient_list=['ostadju@fastmail.com', 'aligholamzadeh42@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'home/success.html')
    return render(request, "home/contactus.html", {'form': form,
                                                   'p': True})


def editprofile(request):
    if request.method == 'GET':
        form = EditProfileForm()
    else:
        form = EditProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            if not Profile.objects.all().filter(user=user).exists():
                user_profile = Profile(user=user, bio=form.cleaned_data['bio'], gender=form.cleaned_data['gender'])
            else:
                user_profile = user.profile
                user_profile.bio = form.cleaned_data['bio']
                user_profile.gender = form.cleaned_data['gender']
                user_profile.image = form.cleaned_data.get('image')
            user_profile.save()
            return HttpResponseRedirect("/profile")
    return render(request, "home/editprofile.html", {'form': form})
