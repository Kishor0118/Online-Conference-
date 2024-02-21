from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_type = models.CharField(max_length=255, choices=[('single', 'Single'), ('group', 'Group')])

class Member(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

class Group(models.Model):
    representative_user = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    group_name = models.CharField(max_length=255)
    member = models.ManyToManyField(Member, related_name='groups')

class Attendee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=255)

class Addon(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=255)

class AddonInstance(models.Model):
    addon = models.ForeignKey(Addon, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    details = models.TextField()

class UserAddon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    addon_instance = models.ForeignKey(AddonInstance, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=255)


