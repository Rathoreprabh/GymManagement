# gymapp/admin.py
from django.contrib import admin
from .models import MembershipPlan, Trainer, Service, Booking, ClassHistory

admin.site.register(MembershipPlan)
admin.site.register(Trainer)
admin.site.register(Service)
admin.site.register(Booking)
admin.site.register(ClassHistory)
