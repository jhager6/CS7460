from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

#added for css/javascript/images
from django.conf import settings
from django.conf.urls.static import static
#------------------------------------

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', 'ideaphase.views.home', name='home'),                    
    url(r'^list/$', 'ideaphase.views.list', name='list'),
    url(r'^profile/$', 'ideaphase.views.profile', name='profile'),
    # url(r'^blog/', include('blog.urls')),
    
)

urlpatterns += static (settings.STATIC_URL, document_root=settings.STATIC_ROOT)

