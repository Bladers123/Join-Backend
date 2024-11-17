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
        fields = '__all__'

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    assigned_to = AssignedSerializer(many=True)
    subtasks = SubtaskSerializer(many=True)

    class Meta:
        model = Ticket
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True)  
    contacts = ContactSerializer(many=True)  

    class Meta:
        model = Profile
        fields =  '__all__'



