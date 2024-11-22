# profile_app/api/serializers.py




from rest_framework import serializers
from ..models import Assigned, Profile, Contact, Subtask, Ticket


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'number', 'backgroundColor', 'isSelected']

class AssignedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)  # Optional, damit neue Einträge erstellt werden können

    class Meta:
        model = Assigned
        fields = ['id', 'name', 'backgroundColor']

class SubtaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)  # Das `id`-Feld ist optional

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

    def validate_subtasks(self, value):
        for subtask in value:
            # Bestehende Subtasks müssen eine ID haben, neue Subtasks nicht
            if 'id' in subtask and not isinstance(subtask['id'], int):
                raise serializers.ValidationError("Subtask 'id' must be an integer.")
        return value



    def create(self, validated_data):
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

    
    def update(self, instance, validated_data):
        # Subtasks aktualisieren
        if 'subtasks' in validated_data:
            subtasks_data = validated_data.pop('subtasks', [])
            subtask_ids = []

            for subtask_data in subtasks_data:
                if 'id' in subtask_data:  # Bestehender Subtask
                    subtask_instance = Subtask.objects.get(id=subtask_data['id'])
                    for key, value in subtask_data.items():
                        setattr(subtask_instance, key, value)
                    subtask_instance.save()
                    subtask_ids.append(subtask_instance.id)
                else:  # Neuer Subtask
                    new_subtask = Subtask.objects.create(ticket=instance, **subtask_data)
                    subtask_ids.append(new_subtask.id)

            instance.subtasks.exclude(id__in=subtask_ids).delete()

        # AssignedTo aktualisieren
        if 'assignedTo' in validated_data:
            assigned_data = validated_data.pop('assignedTo', [])
            assigned_instances = []

            for assigned in assigned_data:
                if 'id' in assigned:  # Bestehender Assigned
                    assigned_instance = Assigned.objects.get(id=assigned['id'])
                    for key, value in assigned.items():
                        setattr(assigned_instance, key, value)
                    assigned_instance.save()
                    assigned_instances.append(assigned_instance)
                else:  # Neuer Assigned
                    new_assigned = Assigned.objects.create(ticket=instance, **assigned)  # Ticket setzen
                    assigned_instances.append(new_assigned)

            instance.assignedTo.set(assigned_instances)

        # Andere Felder aktualisieren
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance









class ProfileSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True)  
    contacts = ContactSerializer(many=True)  

    class Meta:
        model = Profile
        fields =  '__all__'



