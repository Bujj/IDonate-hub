"""homeHub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from homes import views as home_views
from volunteers import views as volunteers_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^homes/', include("homes.urls", namespace='homes')),
    url(r'^events/', include("events.urls", namespace='events')),
    url(r'^accounts/', include('allauth.urls')),

# Volunteers
    url(r'^$', home_views.home_list, name='home'),
    # url(r'^$', volunteers_views.home, name='home'),
    url(r'^about/$', volunteers_views.about, name='about'),
    url(r'^team/$', volunteers_views.team, name='team'),
    url(r'^developers/$', volunteers_views.developers, name='developers'),
    url(r'^profile/$', volunteers_views.userProfile, name='profile'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
