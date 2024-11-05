# auth/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import RegisterSerializer, UserSerializer
from django.contrib.auth.models import User

class RegisterView(APIView):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()  # Alle Benutzer aus der Datenbank abrufen
        serializer = UserSerializer(users, many=True)  # UserSerializer für mehrere Benutzer
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
