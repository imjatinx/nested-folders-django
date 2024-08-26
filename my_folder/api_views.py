from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Folder
from .serializers import FolderSerializer

@api_view(['GET', 'POST'])
def folder_list_create(request, parent_id=None):
    if request.method == 'GET':
        if parent_id:
            folders = Folder.objects.filter(parent_id=parent_id)
        else:
            folders = Folder.objects.filter(parent=None)
        serializer = FolderSerializer(folders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data.copy()
        if parent_id:
            data['parent'] = parent_id
        serializer = FolderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
