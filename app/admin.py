from django.contrib import admin
from .models import Member, Contribution, Goal, Event, Alert

admin.site.register(Member)
admin.site.register(Contribution)
admin.site.register(Goal)
admin.site.register(Event)
admin.site.register(Alert)