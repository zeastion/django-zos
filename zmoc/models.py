#coding=utf-8

from django.db import models

from zasset.models import Staff

class Change(models.Model):

    Type_change = (
        ('UPDATE', u'Update'),
        ('ROLLBACK', u'Rollback'),
        ('TEST', u'Test'),
    )

    uid = models.AutoField(primary_key=True, unique=True)
    commit_id = models.IntegerField(max_length=1024, verbose_name='COMMIT-ID')
    tag_id = models.IntegerField(max_length=1024, verbose_name='TAG-ID')
    stamp = models.DateTimeField(auto_now=True, verbose_name='TIMESTAMP')
    staff = models.ForeignKey(Staff, verbose_name='INITIATOR')
    type = models.CharField(max_length=256, choices=Type_change, verbose_name='CHANGE-TYPE')
    content = models.TextField(verbose_name='CHANGE RECORD')

    def __unicode__(self):
        return self.content