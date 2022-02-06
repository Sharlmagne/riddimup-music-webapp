from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Creates a profile for user everytime a user is created

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Saves profile everytime the User object gets saved

@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    instance.profile.save()