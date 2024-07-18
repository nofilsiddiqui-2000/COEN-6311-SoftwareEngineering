from django.contrib import admin
from .models import EventNotification

@admin.register(EventNotification)
class EventNotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
