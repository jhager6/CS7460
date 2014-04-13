#main settings urls file
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = patterns('',
    (r'^ideaphase/', include('ideaphase.urls')),
    url(r'^', 'ideaphase.views.home'),
    url(r'^list/', 'ideaphase.views.list'),
    url(r'^profile/', 'ideaphase.views.profile'),
    url(r'^admin/', include(admin.site.urls)),

    #(r'^$', RedirectView.as_view(url='/ideaphase/list/')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
