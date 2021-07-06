from django.contrib import admin
from .models import Conference, ConferenceRoom, Tag

admin.site.register(Conference)
admin.site.register(ConferenceRoom)
admin.site.register(Tag)