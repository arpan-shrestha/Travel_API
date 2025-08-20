from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TripViewSet, ActivitiesViewSet

router = DefaultRouter()
router.register(r'trips', TripViewSet)
router.register(r'activities',ActivitiesViewSet)

urlpatterns = router.urls