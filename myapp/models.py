from django.contrib.auth.models import User
from django.db import models
from datetime import date, time as dt_time

class MembershipPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in months", default=1)  # Set default to 1 month
    description = models.TextField()

    def __str__(self):
        return self.name

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    availability = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, default=1)  # Ensure ID 1 exists or update default
    date = models.DateField(default=date.today)  # Use date.today for default date
    time = models.TimeField(default=dt_time(9, 0))  # Default time is set to 9:00 AM

    def __str__(self):
        return f"{self.member} - {self.service} on {self.date} at {self.time}"

class ClassHistory(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, default=1)  # Replace 1 with an existing Booking ID
    attended = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.member} - {self.booking.service} on {self.booking.date}"
