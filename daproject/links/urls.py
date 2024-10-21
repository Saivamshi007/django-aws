from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name=''),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('profile',views.profile,name='profile'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout',views.logout,name='logout'),
    path('delete-account',views.delete_account,name='delete_account'),
]