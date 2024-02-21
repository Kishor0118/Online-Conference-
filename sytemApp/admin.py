from django.contrib import admin
from  .models import Profile,Event,Attendee,Group,Member


admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(Attendee)
admin.site.register(Group)
admin.site.register(Member)
