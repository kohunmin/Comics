from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'comics.views.home', name='home'),    
    url(r'^(?P<book_id>[0-9]+)/$', 'comics.views.page', name='page'),
    url(r'^(?P<book_id>[0-9]+)/(?P<bookpage_id>[0-9]+)/$', 'comics.views.pageDetail', name='pageDetail'),
#    url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

)
