from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Certification, User, Event
from .forms import UserForm, CheckinForm

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CheckinForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            rfid = form.cleaned_data['rfid']
            userkey = User.objects.get(rfid=rfid)
            Event.objects.create(user=userkey, status = 'SE')
            return redirect('/checkin/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CheckinForm()
        return render(request, 'checkin/user_new.html', {'form': form})

def user_new(request):
    if request.method =="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'checkin/user_new.html', {'form': form})

def events(request):
    e_list = Event.objects.all()
    context = {'event_list': e_list}
    return render(request, 'checkin/events.html', context)
