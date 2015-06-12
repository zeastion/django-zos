from django.conf.urls import patterns, url
from zmoc import views

urlpatterns = patterns('',

    url(r'^$', views.zmocindex, name='mocindex'),

)