from django.conf.urls import patterns, url
from zasset import views

urlpatterns = patterns('',

    url(r'^$', views.assetindex, name='assetindex'),
    url(r'^hardware/$', views.hardware, name='hardware'),
    url(r'^software/$', views.software, name='software'),

)