from django.contrib import admin

# Register your models here.
from .models import Organization, Event

admin.site.register(Organization)
admin.site.register(Event)
