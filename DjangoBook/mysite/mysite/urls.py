# from django.conf.urls import patterns, include, url

# # Uncomment the next two lines to enable the admin:
# # from django.contrib import admin
# # admin.autodiscover()

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'mysite.views.home', name='home'),
#     # url(r'^mysite/', include('mysite.foo.urls')),

#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#     # Uncomment the next line to enable the admin:
#     # url(r'^admin/', include(admin.site.urls)),
# )

# from django.conf.urls.defaults import *
# from mysite.views import hello

# urlpatterns = patterns('',
#     ('^hello/$', hello),
# )

# from django.conf.urls.defaults import *
# from mysite.views import hello, current_datetime

# urlpatterns = patterns('',
#     ('^hello/$', hello),
#     ('^time/$', current_datetime),
#     ('^another-time-page/$', current_datetime),
# )

from django.contrib import admin
admin.autodiscover()
from django.conf.urls.defaults import *
#from mysite.views import hello, current_datetime, hours_ahead
from books import views

urlpatterns = patterns('',
    # (r'^hello/$', hello),
    # (r'^time/$', current_datetime),
    # (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^admin/', include(admin.site.urls)),
    #(r'^search-form/$', views.search_form),
    (r'^search/$', views.search),
    (r'^contact/$', views.contact),
)


#from books import views

# urlpatterns = patterns('',
#     # ...
#     (r'^search-form/$', views.search_form),
#     # ...
# )
