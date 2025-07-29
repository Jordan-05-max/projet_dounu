# accounts/api_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import CustomUser

class UserList(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
