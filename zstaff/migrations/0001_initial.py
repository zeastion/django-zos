# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dname', models.CharField(unique=True, max_length=24)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sname', models.CharField(unique=True, max_length=24)),
                ('gender', models.CharField(max_length=1, verbose_name=b'gender', choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('birth', models.DateTimeField(verbose_name=b'Birthday')),
                ('phone', models.CharField(unique=True, max_length=32)),
                ('email', models.EmailField(max_length=75)),
                ('depart', models.ForeignKey(to='zstaff.Department')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
