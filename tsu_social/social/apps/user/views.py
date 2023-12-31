from rest_framework.response import Response    
from rest_framework import viewsets

from apps.user.serializer import UserSerializer
from apps.user.models import User


# Create your views here.
class UserViewSet(viewsets.ViewSet):

    model = User
    serializer = UserSerializer

    def list(self, request, *args, **kwargs):
        users = self.model.objects.all()
        serializer = self.serializer(users, many=True)

        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        print(request.data)
        return Response({'x': 'y'})