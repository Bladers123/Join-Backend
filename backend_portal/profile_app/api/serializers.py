# profile_app/api/serializers.py




from rest_framework import serializers
from ..models import Profile, Contact
from tickets_app.models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'number', 'backgroundColor', 'isSelected']


class ProfileSerializer(serializers.ModelSerializer):
    ticket = TicketSerializer(many=True)  
    contacts = ContactSerializer(many=True)  

    class Meta:
        model = Profile
        fields = ['user', 'ticket', 'contacts']
