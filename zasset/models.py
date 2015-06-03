#coding=utf-8
from django.db import models


class Department(models.Model):
    dname = models.CharField(max_length=24, unique=True)

    def __unicode__(self):
        return self.dname

class Staff(models.Model):
    sname = models.CharField(max_length=24, unique=True)
    gender = models.CharField('gender', choices=(('M','Male'),('F','Female')), max_length=1)
    birth = models.DateField('Birthday')
    depart = models.ForeignKey(Department)
    phone = models.CharField(max_length=32, unique=True)
    email = models.EmailField()

    def __unicode__(self):
        return self.sname


class Hardware(models.Model):
    hostname = models.CharField(max_length=24, unique=True)
    staff = models.ForeignKey(Staff)
    ostype = models.CharField(max_length=32)
    ram = models.CharField(max_length=12)
    ipv4 = models.IPAddressField(unique=True)
    function = models.CharField('function', choices=(('Development','development'), ('Operation', 'operation'), ('Test', 'test')), max_length=24)

    def __unicode__(self):
        return self.hostname