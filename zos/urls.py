from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^&', include('zuser.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^zuser/', include('zuser.urls')),
    url(r'^zasset/', include('zasset.urls')),
    url(r'^zmoc/', include('zmoc.urls')),

)
