from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('کاربری با ایمیل وارد شده وجود دارد')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError('کاربری با نام کاربری وارد شده وجود دارد')
        return username

    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')
        password1 = self.cleaned_data.get('password1')
        if password1 != password2:
            raise forms.ValidationError('گذرواژه و تکرار گذرواژه یکسان نیستند')
        return password1


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    gender = models.CharField(
        max_length=1, choices=(('M', 'Male'), ('F', 'Female')),
        blank=True, null=True)
