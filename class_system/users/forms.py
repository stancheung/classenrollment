from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import CustomUser
from django.core.validators import RegexValidator

class CustomForm(forms.ModelForm):
    password = forms.CharField(max_length=32)
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'gender', 'age', 'phone_num', 'emergency_contact_name', 'emergency_contact_num']