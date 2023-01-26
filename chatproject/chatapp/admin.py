from django.contrib import admin
from .models import Messages, Room

admin.site.register(Room)
admin.site.register(Messages)
