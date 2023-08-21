from rest_framework.routers import DefaultRouter

from apps.groups.views import GroupsViewSet


router = DefaultRouter()
router.register(r'', GroupsViewSet, basename='groups')
urlpatterns = router.urls
