from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('products', ProductViewSet, basename='product')
router.register('orders', OrderViewSet, basename='order')
router.register('categories', CategoryViewSet, basename='category')
router.register('cart', CartViewSet, basename='cart')

urlpatterns = [
    path('me/', current_user, name='current_user'),
    path('', include(router.urls)),
]
