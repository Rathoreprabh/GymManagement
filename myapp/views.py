from django.shortcuts import render, redirect
from .models import MembershipPlan, Service, Trainer, Booking
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def home(request):
    return render(request, 'myapp/home.html')

@login_required
def membership_plans(request):
    plans = MembershipPlan.objects.all()
    return render(request, 'myapp/membership_plans.html', {'plans': plans})

@login_required
def services(request):
    services = Service.objects.all()
    return render(request, 'myapp/services.html', {'services': services})

@login_required
def trainers(request):
    trainers = Trainer.objects.all()
    return render(request, 'myapp/trainers.html', {'trainers': trainers})

@login_required
def book_service(request):
    services = Service.objects.all()
    if request.method == 'POST':
        service_id = request.POST.get('service')
        date = request.POST.get('date')
        time = request.POST.get('time')
        # Add validation for date and time if necessary
        Booking.objects.create(member=request.user, service_id=service_id, date=date, time=time)
        return redirect('booking_history')
    return render(request, 'myapp/book_service.html', {'services': services})

@login_required
def booking_history(request):
    bookings = Booking.objects.filter(member=request.user)
    return render(request, 'myapp/booking_history.html', {'bookings': bookings})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'myapp/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')
