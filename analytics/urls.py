from django.conf.urls.defaults import patterns, url
from views import *

urlpatterns = patterns('',
	url(r'^hits/?$', hits_per_interval),
	url(r'^hits/(?P<days>[0-9]+)/?$', hits_per_interval),
)
