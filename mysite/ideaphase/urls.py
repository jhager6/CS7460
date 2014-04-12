from django.conf.urls import patterns, url

urlpatterns = patterns('ideaphase.views',
    url(r'^list/$', 'list', name='list'),
)
