from rest_framework import serializers
from .models import Folder

class FolderSerializer(serializers.ModelSerializer):
    subfolders = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Folder
        fields = ['id', 'name', 'parent', 'subfolders', 'created_at']
