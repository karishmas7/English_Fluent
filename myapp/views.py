from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm,UserProfileForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django import forms
from .models import UserProfile
from .models import LearnSpokenEnglish
# from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import views as auth_views


# Create your views here.
def Basepage(request):
	return render(request,"base.html")

def LoginView(request):
	if request.method=='POST':
		form=LoginForm(request.POST)
		if form.is_valid():
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			user=authenticate(request,username=username,password=password)
			if user is not None:
				login(request,user)
				messages.success(request,"You have Login Succesfully")
				return render(request,"logouthead.html")
			else:
				messages.error(request,"We couldn't find an account with that name. Try another or get a New Acoount")
				return render(request,"login.html",{'form':form})
	else:
		form=LoginForm()
		return render(request,"login.html",{'form':form})


def LogoutView(request):
	logout(request)
	messages.success(request,"You have been Logout Successfully")
	return render(request,'logout.html')
		

def RegisterView(request):
	if request.method=='POST':
		Register_form=RegisterForm(request.POST)
		UserProfile_form=UserProfileForm(request.POST)
		if Register_form.is_valid() and UserProfile_form.is_valid():
			Registerform=Register_form.save()
			UserProfileform=UserProfile_form.save(commit=False)
			Address=UserProfile_form.cleaned_data['Address']
			City=UserProfile_form.cleaned_data['City']
			State=UserProfile_form.cleaned_data['State']
			profile=UserProfile(user=Registerform,Address=Address,City=City,State=State)
			profile.save()
			messages.success(request,"You have been Register Successfully")
			return redirect('login')
		else:
			messages.error(request,"You have not Entered correct Data!")
			return redirect('register')
	else:
		Register_form=RegisterForm()
		UserProfile_form=UserProfileForm()
		return render(request,"register.html",{'Register_form':Register_form,'UserProfile_form':UserProfile_form})


def home(request):
	return render(request,'home.html')


def contact(request):
	return render(request,'contactus.html')

def learnenglish(request):
	dataenglish=LearnSpokenEnglish.objects.all()
	dh={
		'dataenglish':dataenglish
	}
	return render(request,'learnenglish.html',dh)

def learnspokenenglish(request):
	return render(request,"learnspokenenglish.html")

    
    