from django.shortcuts import render

from django.http import HttpResponse

from .models import Certification, User, Event

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def users(request):
    return 0

def events(request):
    e_list = Event.objects.all()
    context = {'event_list': e_list}
    return render(request, 'checkin/events.html', context)
