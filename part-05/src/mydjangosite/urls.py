from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mydjangosite.views.home', name='home'),
    # url(r'^mydjangosite/', include('mydjangosite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^blog/$', 'blog.views.index'),
    url(r'^blog/details/(?P<id>\d+)/$', 'blog.views.details'),
)
