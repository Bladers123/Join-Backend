# profile_app/api/urls.py

from django.urls import path
from .views import AssignedContactDetailView, AssignedTicketsDetailView, AssignedTicketsView, ProfileDetailView, AssigendContactsView

urlpatterns = [
    path('', ProfileDetailView.as_view(), name='profile-detail'),
    path('contacts/', AssigendContactsView.as_view(), name='assigned-contacts'),
    path('contacts/<int:pk>/', AssignedContactDetailView.as_view(), name='contact-detail'),
    path('tickets/', AssignedTicketsView.as_view(), name='tickets'),
    path('tickets/<int:pk>/', AssignedTicketsDetailView.as_view(), name='ticket-detail')
]
