from django.contrib import admin
# gymapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('membership-plans/', views.membership_plans, name='membership_plans'),
    path('services/', views.services, name='services'),
    path('trainers/', views.trainers, name='trainers'),
    path('book-service/', views.book_service, name='book_service'),
    path('booking-history/', views.booking_history, name='booking_history'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
]

