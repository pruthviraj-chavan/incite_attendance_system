from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import StudentProfile

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    address = forms.CharField(widget=forms.Textarea)
    course = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "phone", "address", "course"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['phone', 'address', 'course']