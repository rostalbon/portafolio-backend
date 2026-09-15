from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView as ApiView

from projects.models import ProjectsTable
from projects.serializers import ProjectSerializer

class ProjectView(ApiView):
    def get(self, request):
        projects = ProjectsTable.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)