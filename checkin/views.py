from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Certification, User, Event
from .forms import UserForm

def index(request):

    return HttpResponse("Hello, world. You're at the polls index.")

def user_new(request):
    if request.method =="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'checkin/user_new.html', {'form': form})

def events(request):
    e_list = Event.objects.all()
    context = {'event_list': e_list}
    return render(request, 'checkin/events.html', context)
