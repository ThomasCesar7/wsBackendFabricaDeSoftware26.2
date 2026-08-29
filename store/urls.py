from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet,
    ProductViewSet,
    OrderViewSet,
    OrderItemViewSet,
    AddressViewSet
)


router = DefaultRouter()

router.register(
    'categories',
    CategoryViewSet
)

router.register(
    'products',
    ProductViewSet
)

router.register(
    'orders',
    OrderViewSet
)

router.register(
    'order-items',
    OrderItemViewSet
)

router.register(
    'addresses',
    AddressViewSet
)


urlpatterns = router.urls