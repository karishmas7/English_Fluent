from django.contrib import admin
from .models import UserProfile
from .models import LearnSpokenEnglish
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
	list_display=['user','Address','City','State']
admin.site.register(UserProfile,UserProfileAdmin)

admin.site.register(LearnSpokenEnglish)
class LearnSpokenEnglishAdmin(admin.ModelAdmin):
	list_display1=['Title','body']