# views.py




from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer, UserOverviewSerializer
from django.contrib.auth import get_user_model



User = get_user_model()

class RegisterView(APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAdminUser()]  # Nur Admins und Staff-Benutzer dürfen GET verwenden
        return [AllowAny()]  # POST ist für alle zugänglich

    def get(self, request, *args, **kwargs):
        users = User.objects.all()  # Alle Benutzer aus der Datenbank abrufen
        serializer = UserOverviewSerializer(users, many=True)  # Serializer für mehrere Benutzer
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class LoginAPIView(APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAdminUser()]  # Nur Admins und Staff-Benutzer dürfen GET verwenden
        return [AllowAny()]  # POST ist für alle zugänglich
    
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserOverviewSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Benutzer aus den validierten Daten holen
        user = serializer.validated_data['user']
        
        # Token abrufen oder erstellen
        token, created = Token.objects.get_or_create(user=user)
        
        # Token und Benutzerdaten zurückgeben
        return Response({
            "user_id": user.id,
            "username": user.username,
            "email": user.email,
            "token": token.key
        }, status=status.HTTP_200_OK)







