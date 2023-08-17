from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from .views import UserViewSet



urlpatterns = [
    path('', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name=''),
]