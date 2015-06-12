from django.conf.urls import patterns, url
from zasset import views

urlpatterns = patterns('',

    url(r'^$', views.zassetindex, name='assetindex'),
    url(r'^hardware/$', views.hardware, name='hardware'),
    url(r'^software/$', views.software, name='software'),
    url(r'^staffindex/$', views.zstaffindex, name='zstaffindex'),
    url(r'^staff/$', views.zstaff, name='zstaff'),
    url(r'^department/$', views.zdepartment, name='zdepartment'),

)