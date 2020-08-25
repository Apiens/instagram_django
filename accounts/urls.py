from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('edit/', views.profile_edit, name='profile_edit'),
    path('password_change/', views.password_change, name='password_change'),
    #path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
]
    
# accounts/login/ => settings.LOGIN_URL
# login required사용시 settings.LOGIN_URL로 redirect.