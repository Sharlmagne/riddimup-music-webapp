from django.contrib import admin
from .models import Comment, Profile, Track

admin.site.register(Profile)
admin.site.register(Track)
admin.site.register(Comment)

