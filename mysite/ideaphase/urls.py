from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

#added for css/javascript/images
from django.conf import settings
from django.conf.urls.static import static
#------------------------------------

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('ideaphase.views',
    url(r'^home/$', 'home', name='home'),                    
    url(r'^list/$', 'list', name='list'),
    url(r'^profile/$', 'profile', name='profile'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
)

urlpatterns += static (settings.STATIC_URL, document_root=settings.STATIC_ROOT)

