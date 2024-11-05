# views.py




from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, AllowAny
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterView(APIView):

    def get_permissions(self):
        """
        Erlaubt den Zugriff auf GET nur für Admins und Staff-Benutzer.
        POST ist für alle zugänglich.
        """
        if self.request.method == 'GET':
            return [IsAdminUser()]  # Nur Admins und Staff-Benutzer dürfen GET verwenden
        return [AllowAny()]  # POST ist für alle zugänglich

    def get(self, request, *args, **kwargs):
        users = User.objects.all()  # Alle Benutzer aus der Datenbank abrufen
        serializer = RegisterSerializer(users, many=True)  # Serializer für mehrere Benutzer
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







