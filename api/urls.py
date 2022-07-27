from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from api.models import Rater
from .views import ProductViewSet, RaterViewSet

router = routers.DefaultRouter()
router.register('product', ProductViewSet)
router.register('rater', RaterViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
