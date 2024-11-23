from django.urls import path
from .views import RegisterView, LoginAPIView, UsersView, UserDetailView, RegisterGuestView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('register_guest/', RegisterGuestView.as_view(), name='register-guest'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('users/', UsersView.as_view(), name='users'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail')
]