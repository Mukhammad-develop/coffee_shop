from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('products', ProductViewSet, basename='product')
router.register('orders', OrderViewSet, basename='order')
router.register('categories', CategoryViewSet, basename='category')
router.register('cart', CartViewSet, basename='cart')

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('authentication/', AuthenticationView.as_view(), name='authentication'),
    path('verification/', VerificationView.as_view(), name='verification'),
    path('me/', CurrentUserView.as_view(), name='me'),
    path('', include(router.urls)),
]
