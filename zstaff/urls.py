from django.conf.urls import patterns, url
from zstaff import views

urlpatterns = patterns('',

    url(r'^$', views.zstaffindex, name='zstaffindex'),
    url(r'^staff/$', views.zstaff, name='zstaff'),
    url(r'^department/$', views.zdepartment, name='zdepartment')

)
