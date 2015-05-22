from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    dep = models.CharField(max_length=10)

    def __unicode__(self):
        return self.user.username
