#coding=utf-8
from django.db import models

from zstaff.models import Staff


class Hardware(models.Model):
    owner = models.ForeignKey(Staff)
    hostname = models.CharField(max_length=24)
    ostype = models.CharField(max_length=32)
    ipv4 = models.IPAddressField()

    def __unicode__(self):
        return self.hostname