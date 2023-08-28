from django.db import models
from django.contrib.auth.admin import User
from  django.dispatch import receiver
from django.db.models.signals import post_save


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    nickname = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username

# when a new User is saved to the database 
# the signal will be captured
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Member(user=instance)
        user_profile.save()
