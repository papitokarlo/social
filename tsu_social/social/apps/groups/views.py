from rest_framework.response import Response    
from rest_framework import viewsets, status

from apps.groups.models import Groups
from apps.groups.serializer import GroupsSerializer
from apps.user.models import User


# Create your views here.
class GroupsViewSet(viewsets.ViewSet):

    model = Groups
    serializer = GroupsSerializer

    def list(self, request, *args, **kwargs)-> Response:
        groups = self.model.objects.all()
        serializer = self.serializer(groups, many=True)

        for creator_id in serializer.data:
            user = User.objects.get(id=creator_id['creator']).user_name
            creator_id['creator'] = user
            
        return Response(serializer.data)

    def create(self, request, *args, **kwargs)-> Response:
        name = request.data.get('name')
        name_in = Groups.objects.filter(name=name)
        if name_in:
            return Response({"message": "Group already exists"}, status=status.HTTP_400_BAD_REQUEST)

        groups_data = request.data.copy()
        groups_data['members_count'] = 1
        groups_data['creator'] = 982392183647326

        serializer = self.serializer(data=groups_data)
        if serializer.is_valid():
            serializer.save() 
            return Response({"message": "Group created successfully"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

