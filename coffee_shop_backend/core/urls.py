from django.urls import path
from .views import RegisterUserView, current_user

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('me/', current_user, name='current_user'),
]
