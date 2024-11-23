# profile_app/api/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models import Contact, Profile, Subtask, Task
from .serializers import ProfileSerializer, ContactSerializer, SubtaskSerializer, TaskSerializer



class ProfilesView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data, status=200)


class ProfileDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data, status=200)
        except Profile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=404)
                         

class ContactsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile, created = Profile.objects.get_or_create(user=request.user)
        contacts = profile.contacts.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()
            profile, created = Profile.objects.get_or_create(user=request.user)
            profile.contacts.add(contact) 
            profile.save() 
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

class ContactDetailView(APIView):
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


    

class TasksView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        tasks = profile.tasks.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            profile, created = Profile.objects.get_or_create(user=request.user)
            profile.tasks.add(task) 
            profile.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

class TaskDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response({"error": "task not found"}, status=404)

    def put(self, request, pk):
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
        profile.tasks.remove(task)
        if not Profile.objects.filter(tasks=task).exists():
            task.delete()
        return Response({"message": "task deleted successfully"}, status=204)


class SubtasksView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            profile = Profile.objects.get(user=request.user)
            tasks = profile.tasks.all()
            result = []
            for task in tasks:
                subtasks = task.subtasks.all()
                subtasks_serializer = SubtaskSerializer(subtasks, many=True)
                result.append({
                    "task_id": task.id,
                    "task_title": task.title,
                    "subtasks": subtasks_serializer.data
                })
            return Response(result, status=200)
        except Profile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=404)

    
class SubtaskDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            profile = Profile.objects.get(user=request.user)
            subtask = Subtask.objects.get(pk=pk)
            if not subtask.task in profile.tasks.all():
                return Response({"error": "Permission denied"}, status=403)
            serializer = SubtaskSerializer(subtask)
            return Response(serializer.data, status=200)
        except Profile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=404)
        except Subtask.DoesNotExist:
            return Response({"error": "Subtask not found"}, status=404)
  
