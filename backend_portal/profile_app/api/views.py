# profile_app/api/views.py





from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from ..models import Profile
from .serializers import ProfileSerializer, ContactSerializer

class ProfileDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Versuche, das Profil abzurufen
        profile, created = Profile.objects.get_or_create(user=request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)





class AssigendContactsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Profil des aktuellen Nutzers abrufen
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            return Response({"error": "Profile does not exist"}, status=404)

        # Kontakte des Profils abrufen
        contacts = profile.contacts.all()

        # Kontakte serialisieren
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()
            # Kontakt dem Profil des aktuellen Nutzers hinzufügen
            profile, created = Profile.objects.get_or_create(user=request.user)
            profile.contacts.add(contact)  # Verknüpfen
            profile.save()  # Speichern
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



    