#main settings urls file
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^ideaphase/', include('ideaphase.urls')),
    url(r'^', 'ideaphase.views.home'),
    url(r'^list/', 'ideaphase.views.list'),
    url(r'^profile/', 'ideaphase.views.profile'),
    url(r'^logout/', 'ideaphase.views.logout'),
    url(r'^browse_contest_ideas/', 'ideaphase.views.browse_contest_ideas'),
    url(r'^contest_landing_page/', 'ideaphase.views.contest_landing_page'),
    url(r'^profile_my_submissions/', 'ideaphase.views.profile_my_submissions'),
    url(r'^submit_idea/', 'ideaphase.views.submit_idea'),

    #(r'^admin/', RedirectView.as_view(url=os.path.join(BASE_DIR, '/mysite/admin')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
