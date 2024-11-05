# serializers.py




from rest_framework import serializers
from django.contrib.auth.models import User
from profile_app.models import Profile

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField()  # Überschreibt das username-Feld mit eigener Validierung

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_username(self, value):
        # Erlaubt Leerzeichen im Benutzernamen, entfernt führende und nachgestellte Leerzeichen
        value = value.strip()
        
        # Benutzername darf nicht leer sein
        if not value:
            raise serializers.ValidationError("Username shouldn't be empty.")
        
        # Prüfen, ob der Benutzername bereits existiert
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken.")
        return value

    
    def validate_email(self, value):
        """
        Prüft, ob die E-Mail-Adresse bereits verwendet wird.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This e-mail address is already in use.")
        return value

    def create(self, validated_data):
        # Benutzer erstellen, Leerzeichen im Benutzernamen sind erlaubt
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        Profile.objects.create(user=user)  # Profil für den Benutzer erstellen
        return user
