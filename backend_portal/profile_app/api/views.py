# profile_app/api/views.py





from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from ..models import Contact, Profile, Task
from .serializers import ProfileSerializer, ContactSerializer, TaskSerializer

class ProfileDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile, created = Profile.objects.get_or_create(user=request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)





class AssigendContactsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Profil des aktuellen Nutzers abrufen oder erstellen
        profile, created = Profile.objects.get_or_create(user=request.user)

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
    


class AssignedContactDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            contact = Contact.objects.get(pk=pk)
            serializer = ContactSerializer(contact)
            return Response(serializer.data)
        except Contact.DoesNotExist:
            return Response({"error": "Contact not found"}, status=404)


    def put(self, request, pk):
        try:
            contact = Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            return Response({"error": "Contact not found"}, status=404)
        
        serializer = ContactSerializer(contact, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


    def delete(self, request, pk):
        try:
            contact = Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            return Response({"error": "Contact not found"}, status=404)

        profile = Profile.objects.get(user=request.user)
        profile.contacts.remove(contact)

        if not Profile.objects.filter(contacts=contact).exists():
            contact.delete()

        return Response({"message": "Contact deleted successfully"}, status=204)


    

class AssignedTasksView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        tasks = profile.tasks.all()  # Zugriff auf das ManyToManyField 'task'
        serializer = TaskSerializer(tasks, many=True)  # Verwende den passenden Serializer
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            # Kontakt dem Profil des aktuellen Nutzers hinzufügen
            profile, created = Profile.objects.get_or_create(user=request.user)
            profile.tasks.add(task)  # Verknüpfen
            profile.save()  # Speichern
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

class AssignedTasksDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response({"error": "task not found"}, status=404)

    def put(self, request, pk):
        # print("Raw request data:", request.data)
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({"error": "task not found"}, status=404)

        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({"error": "task not found"}, status=404)

        profile = Profile.objects.get(user=request.user)
        profile.tasks.remove(task)  # Korrektur hier

        # Prüfen, ob kein anderes Profil mehr mit diesem task verknüpft ist
        if not Profile.objects.filter(tasks=task).exists():
            task.delete()

        return Response({"message": "task deleted successfully"}, status=204)

