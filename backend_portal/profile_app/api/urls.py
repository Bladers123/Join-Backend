# profile_app/api/urls.py

from django.urls import path
from .views import ProfileDetailView, AssigendContactsView, AssignedContactDetailView

urlpatterns = [
    path('', ProfileDetailView.as_view(), name='profile-detail'),
    path('contacts/', AssigendContactsView.as_view(), name='assigned-contacts'),
    path('contacts/<int:pk>/', AssignedContactDetailView.as_view(), name='contact-detail'),

]
