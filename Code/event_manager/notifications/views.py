from django.shortcuts import render
from .models import EventNotification

def event_list(request):
    events = EventNotification.objects.all().order_by('date')
    return render(request, 'notifications/event_list.html', {'events': events})
