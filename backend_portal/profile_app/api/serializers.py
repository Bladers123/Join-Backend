from rest_framework import serializers
from ..models import Assigned, Profile, Contact, Subtask, Task


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'number', 'backgroundColor', 'isSelected']

class AssignedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False) 

    class Meta:
        model = Assigned
        fields = ['id', 'name', 'backgroundColor']

class SubtaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Subtask
        fields = ['id', 'title', 'completed']


class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True)
    assignedTo = AssignedSerializer(many=True)

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'dueDate', 'priority', 'category', 'progress', 'subtasks', 'assignedTo'
        ]

    def validate_subtasks(self, value):
        for subtask in value:
            if 'id' in subtask and not isinstance(subtask['id'], int):
                raise serializers.ValidationError("Subtask 'id' must be an integer.")
        return value

    def validate_assignedTo(self, value):
        for assigned in value:
            if 'id' in assigned and not isinstance(assigned['id'], int):
                raise serializers.ValidationError("AssignedTo 'id' must be an integer.")
        return value


    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        assigned_data = validated_data.pop('assignedTo', [])
        task = Task.objects.create(**validated_data)
        for subtask_data in subtasks_data:
            Subtask.objects.create(task=task, **subtask_data)
        for assigned_data in assigned_data:
            Assigned.objects.create(task=task, **assigned_data)
        return task

    
    def update(self, instance, validated_data):
        if 'subtasks' in validated_data:
            subtasks_data = validated_data.pop('subtasks', [])
            subtask_ids = []
            for subtask_data in subtasks_data:
                if 'id' in subtask_data:  
                    subtask_instance = Subtask.objects.get(id=subtask_data['id'])
                    for key, value in subtask_data.items():
                        setattr(subtask_instance, key, value)
                    subtask_instance.save()
                    subtask_ids.append(subtask_instance.id)
                else: 
                    new_subtask = Subtask.objects.create(task=instance, **subtask_data)
                    subtask_ids.append(new_subtask.id)
            instance.subtasks.exclude(id__in=subtask_ids).delete()

        if 'assignedTo' in validated_data:
            assigned_data = validated_data.pop('assignedTo', [])
            assigned_ids = []
            for assigned in assigned_data:
                if 'id' in assigned:
                    try:
                        assigned_instance = Assigned.objects.get(id=assigned['id'])
                        for key, value in assigned.items():
                            setattr(assigned_instance, key, value)
                        assigned_instance.save()
                        assigned_ids.append(assigned_instance.id)
                    except Assigned.DoesNotExist:
                        new_assigned = Assigned.objects.create(task=instance, **assigned)
                        assigned_ids.append(new_assigned.id)
                else:
                    new_assigned = Assigned.objects.create(task=instance, **assigned)
                    assigned_ids.append(new_assigned.id)
            instance.assignedTo.exclude(id__in=assigned_ids).delete()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance










class ProfileSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, required=False)  
    contacts = ContactSerializer(many=True, required=False)  

    class Meta:
        model = Profile
        fields =  '__all__'



