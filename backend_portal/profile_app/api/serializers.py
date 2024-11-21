# profile_app/api/serializers.py




from rest_framework import serializers
from ..models import Assigned, Profile, Contact, Subtask, Ticket


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'number', 'backgroundColor', 'isSelected']

class AssignedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assigned
        fields = ['id', 'name', 'backgroundColor']

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ['id', 'title', 'completed']

class TicketSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True)  # Nested Serializer für Subtasks
    assignedTo = AssignedSerializer(many=True)  # Nested Serializer für AssignedTo

    class Meta:
        model = Ticket
        fields = [
            'id', 'title', 'description', 'dueDate', 'priority', 'category', 'progress', 'subtasks', 'assignedTo'
        ]

    def create(self, validated_data):
        # Subtasks und Assigned werden aus den Daten extrahiert
        subtasks_data = validated_data.pop('subtasks', [])
        assigned_data = validated_data.pop('assignedTo', [])
        
        # Ticket erstellen
        ticket = Ticket.objects.create(**validated_data)
        
        # Subtasks erstellen und verknüpfen
        for subtask_data in subtasks_data:
            Subtask.objects.create(ticket=ticket, **subtask_data)
        
        # AssignedTo erstellen und verknüpfen
        for assigned_data in assigned_data:
            Assigned.objects.create(ticket=ticket, **assigned_data)
        
        return ticket



class ProfileSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True)  
    contacts = ContactSerializer(many=True)  

    class Meta:
        model = Profile
        fields =  '__all__'



