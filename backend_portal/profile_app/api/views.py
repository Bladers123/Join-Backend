# profile/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Profile
from .serializers import ProfileSerializer
from django.contrib.auth.models import User

class ProfileView(APIView):
    """
    GET und PUT für das Benutzerprofil
    """
    def get(self, request, user_id, *args, **kwargs):
        try:
            profile = Profile.objects.get(user_id=user_id)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, user_id, *args, **kwargs):
        try:
            profile = Profile.objects.get(user_id=user_id)
            serializer = ProfileSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Profile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)
