# profile_app/api/urls.py

from django.urls import path
from .views import AssignedContactDetailView, AssignedTasksDetailView, AssignedTasksView, ProfileDetailView, AssigendContactsView

urlpatterns = [
    path('profile/', ProfileDetailView.as_view(), name='profile-detail'),
    path('contacts/', AssigendContactsView.as_view(), name='assigned-contacts'),
    path('contacts/<int:pk>/', AssignedContactDetailView.as_view(), name='contact-detail'),
    path('tasks/', AssignedTasksView.as_view(), name='tasks'),
    path('tasks/<int:pk>/', AssignedTasksDetailView.as_view(), name='task-detail')
]
