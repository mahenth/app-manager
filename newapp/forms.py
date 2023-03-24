from django import forms
from .models import AndroidApp
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AndroidAppForm(forms.ModelForm):
    class Meta:
        model = AndroidApp
        fields = ('name', 'download_link', 'category', 'sub_category')


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('image', 'title', 'link', 'points')


class ScreenshotForm(forms.Form):
    screenshot = forms.ImageField()