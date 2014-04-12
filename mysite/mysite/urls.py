from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = patterns('',
    url(r'^', 'ideaphase.views.list'),
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    (r'^ideaphase/', include('ideaphase.urls')),
    (r'^$', RedirectView.as_view(url='/ideaphase/list/')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
