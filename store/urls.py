from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet,
    ProductViewSet,
    OrderViewSet,
    OrderItemViewSet,
    AddressViewSet,
)


router = DefaultRouter()

router.register(
    'categories',
    CategoryViewSet,
    basename='category'
)

router.register(
    'products',
    ProductViewSet,
    basename='product'
)

router.register(
    'orders',
    OrderViewSet,
    basename='order'
)

router.register(
    'order-items',
    OrderItemViewSet,
    basename='order-item'
)

router.register(
    'addresses',
    AddressViewSet,
    basename='address'
)


urlpatterns = router.urls