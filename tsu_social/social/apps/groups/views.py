from rest_framework.response import Response    
from rest_framework import viewsets, status

from apps.groups.models import Groups
from apps.groups.serializer import GroupsSerializer


# Create your views here.
class GroupsViewSet(viewsets.ViewSet):

    model = Groups
    serializer = GroupsSerializer

    def list(self, request, *args, **kwargs):
        groups = self.model.objects.all()
        serializer = self.serializer(groups, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs)-> Response:
        groups_data = request.data.copy()
        groups_data['creator'] = 1
        # groups_data['members'] = [1]
        # groups_data['admins'] = [1]

        serializer = self.serializer(data=groups_data)
        if serializer.is_valid():
            serializer.save() 
            return Response({"message": "Group created successfully"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

