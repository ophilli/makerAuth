from django.contrib import admin

from .models import Certification, User, Event

class UserAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'username', 'cuid', 'rfid', 'cert_group']
    list_display = ('__str__', 'cuid', 'get_certs', 'get_visit_count')
    search_fields = ['username']

admin.site.register(Certification)
admin.site.register(User, UserAdmin)
admin.site.register(Event)
