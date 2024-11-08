from rest_framework import serializers
from ..models import Ticket, AssignedUser, Subtask

class AssignedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignedUser
        fields = ['name', 'bg_color']

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ['title', 'completed', 'identifier']

class TicketSerializer(serializers.ModelSerializer):
    assigned_to = AssignedUserSerializer(many=True)
    subtasks = SubtaskSerializer(many=True)

    class Meta:
        model = Ticket
        fields = ['id', 'title', 'description', 'due_date', 'priority', 'category', 'assigned_to', 'progress', 'subtasks', 'created_at']
