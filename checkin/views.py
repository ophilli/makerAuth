from django.shortcuts import render

from .models import Certification, User, Event

admin.site.register(Certification)
admin.site.register(User)
admin.site.register(Event)
