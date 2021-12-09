from django.db.models.signals import post_save

from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def created_profile(sender, instance, created, **kwargs):

    if created:
        print('-------------profile is created -----', instance)
        Profile.objects.create(user = instance)


@receiver(post_save, sender = User) # user profile update time signal
def save_profile(sender, instance, **kwargs):
    print('---------inssss-----------',instance)    
    instance.profile.save()
    
    