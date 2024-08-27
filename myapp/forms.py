from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class LoginForm(forms.Form):
	username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))
	password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))


class RegisterForm(UserCreationForm):
	first_name=forms.CharField(label='First Name',widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name=forms.CharField(label='Last Name',widget=forms.TextInput(attrs={'class':'form-control'}))
	username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))
	email=forms.CharField(label='Email Address',widget=forms.TextInput(attrs={'placeholder': 'Enter valid Email Id for Reset Password in Future','class':'form-control'}))
	password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Password Combination of Capital Letter, Symbol, Number','class':'form-control'}))
	password2=forms.CharField(label='ConfirmPassword',widget=forms.PasswordInput(attrs={'class':'form-control'}))
	class Meta:
		model=User
		fields=('first_name','last_name','username','email','password1','password2')

class UserProfileForm(forms.ModelForm):
	Address=forms.CharField(label='Address',widget=forms.TextInput(attrs={'class':'form-control'}))
	City=forms.CharField(label='City',widget=forms.TextInput(attrs={'class':'form-control'}))
	State=forms.CharField(label='State',widget=forms.TextInput(attrs={'class':'form-control'}))
	class Meta:
		model=UserProfile
		fields=('Address','City','State')
	

