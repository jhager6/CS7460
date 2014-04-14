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
    url(r'^logout/$', 'ideaphase.views.logout', name='logout'),
    url(r'^browse_contest_ideas/$', 'ideaphase.views.browse_contest_ideas', name='browse_contest_ideas'),
    url(r'^contest_landing_page/$', 'ideaphase.views.contest_landing_page', name='contest_landing_page'),
    url(r'^profile_my_submissions/$', 'ideaphase.views.profile_my_submissions', name='profile_my_submissions'),
    url(r'^submit_idea/$', 'ideaphase.views.submit_idea', name='submit_idea'),
    # url(r'^blog/', include('blog.urls')),
    
)

urlpatterns += static (settings.STATIC_URL, document_root=settings.STATIC_ROOT)

