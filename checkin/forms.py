from django import forms

from .models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'cuid', 'rfid', 'first_name', 'last_name')

class CheckinForm(forms.Form):
    rfid = forms.CharField(label='RFID', max_length=11) # tied to models.User.rfid
