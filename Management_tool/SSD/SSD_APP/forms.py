from django import forms
from django.forms import ModelForm
from SSD_APP.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# create a forms for your project


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class User_Form(ModelForm):    
    class Meta:
        model = Users
        fields = '__all__'


class UPSI_Form(ModelForm):
    files_data = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
    class Meta:
        model = UPSI
        fields = '__all__'


class DISCLOSURE_Form(ModelForm):    
    class Meta:
        model = DISCLOSURE
        fields = '__all__'