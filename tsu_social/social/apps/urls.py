from django.contrib import admin
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    path('users/', include('apps.user.urls')),
    path('groups/', include('apps.groups.urls')),
]
