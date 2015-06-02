from django.db import models

class Department(models.Model):
    dname = models.CharField(max_length=24, unique=True)

    def __unicode__(self):
        return self.dname

class Staff(models.Model):
    sname = models.CharField(max_length=24, unique=True)
    gender = models.CharField('gender', choices=(('M','Male'),('F','Female')), max_length=1)
    birth = models.DateTimeField('Birthday')
    depart = models.ForeignKey(Department)
    phone = models.CharField(max_length=32, unique=True)
    email = models.EmailField()

    def __unicode__(self):
        return self.sname
