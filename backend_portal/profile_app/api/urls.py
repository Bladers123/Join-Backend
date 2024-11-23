from django.urls import path
from .views import ContactDetailView, TaskDetailView, TasksView, ProfileDetailView, ContactsView, ProfilesView, SubtasksView, SubtaskDetailView

urlpatterns = [
    path('profiles/', ProfilesView.as_view(), name='profiles'),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('contacts/', ContactsView.as_view(), name='assigned-contacts'),
    path('contacts/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
    path('tasks/', TasksView.as_view(), name='tasks'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('subtasks/', SubtasksView.as_view(), name='subtasks'),
    path('subtasks/<int:pk>/', SubtaskDetailView.as_view(), name='subtask-detail'),
]
