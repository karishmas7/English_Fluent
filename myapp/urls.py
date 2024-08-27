from django.contrib import admin
from django.urls import path,include
from .import views
from django.contrib.auth import views as auth_views
# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
    path('home/', views.home,name='home'),
    path('learnspokenenglish/', views.learnspokenenglish,name='learnspokenenglish'),
    path('learnenglish/', views.learnenglish,name='learnenglish'),
    path('contact/', views.contact,name='contact'),
    path('base/', views.Basepage,name='base'),
    path('login/', views.LoginView,name='login'),
    path('logout/', views.LogoutView,name='logout'),
    path('register/', views.RegisterView,name='register'),
    # path('password/', views.change_password, name='change_password'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='change_password.html'),name='change_password'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'),name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),name='password_reset_complete'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, documnet_root=settings.MEDIA_ROOT)