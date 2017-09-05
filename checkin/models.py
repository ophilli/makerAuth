from django.db import models

class Certification(models.Model):
    name = models.CharField(max_length=30)
    # Expiration datetime
    # Prerequisite
    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)  # Used for emails
    cuid = models.CharField(max_length=9, primary_key=True) # Shouldn't change - primary key? | Also good for looking up info
    rfid = models.CharField(max_length=11, unique=True)  # Necessary for RFID scanning
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    join_date = models.DateTimeField('Date Registered', auto_now_add=True) # Interesting user data?
    cert_group = models.ManyToManyField(Certification, blank=True, default=None)

    def get_certs(self):
        return "\n|\n".join([c.name for c in self.cert_group.all()])

    def get_visit_count(self):
        return self.event_set.count()

    def __str__(self):
        return self.first_name + " " + self.last_name

class Event(models.Model):
    timestamp = models.DateTimeField('Time of Event', auto_now_add=True, primary_key=True)

    user = models.ForeignKey('User', on_delete=models.PROTECT)

    SUCCESS = 'SE'
    RFID_NOT_FOUND = 'RNF'

    STATUS_CHOICES = (
        (SUCCESS, 'Successful Entry'),
        (RFID_NOT_FOUND, 'User Not Found'),
    )

    status = models.CharField(
        max_length = 2,
        choices = STATUS_CHOICES,
        default = SUCCESS,
    )

    def __str__(self):
        return self.get_status_display() + " @ " + str(self.timestamp)
