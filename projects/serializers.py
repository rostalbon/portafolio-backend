from rest_framework import serializers
from projects.models import ProjectsTable

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectsTable
        fields = '__all__'