from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
	Address=models.CharField(max_length=100)
	City=models.CharField(max_length=100)
	State=models.CharField(max_length=100)

class LearnSpokenEnglish(models.Model):
	Title=models.CharField(max_length=100)
	body=models.TextField()