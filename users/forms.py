# Описує поля в формі
from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(forms.Form):
    # required=True = Обов'язкове поле для заповнювання
    email = forms.EmailField(label='Введіть Email', required=True)
    username = forms.CharField(label='Введіть Логін',required=True)
    class Meta:
        model = User
        # Порядок виведення форм
        fields = ['username', 'email']