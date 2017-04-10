from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from homes import views as home_views


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^', include("homes.urls", namespace='homes')),

    
    url(r'^create/$', home_views.home_create),
    url(r'^(?P<slug>[\w-]+)/$', home_views.home_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', home_views.home_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', home_views.home_delete),

# # Volunteers
#     url(r'^$', volunteers_views.home, name='home'),
#     url(r'^about/$', volunteers_views.about, name='about'),
#     url(r'^team/$', volunteers_views.team, name='team'),
#     url(r'^developers/$', volunteers_views.developers, name='developers'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
