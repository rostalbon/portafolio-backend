from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView as ApiView

from projects.models import ProjectsTable
from projects.serializers import ProjectSerializer

class ProjectView(ApiView):
    def get(self, request):
        project_id = request.data.get("id")
        if project_id:
            try:
                project = ProjectsTable.objects.get(pk=project_id)
                serializer = ProjectSerializer(project)
                return Response(serializer.data, status=200)
            except ProjectsTable.DoesNotExist:
                return Response(
                    {"error": "Proyecto no encontrado."},
                    status=404
                )
        projects = ProjectsTable.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=200)
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    def delete(self, request):
        project_id = request.data.get("id")
        if not project_id:
            return Response(
                {"error": "Se requiere el ID para eliminar."},
                status=400
            )
        try:
            project = ProjectsTable.objects.get(pk=project_id)
        except ProjectsTable.DoesNotExist:
            return Response(
                {"error": "Proyecto no encontrado."},
                status=404
            )
        project.delete()
        return Response(status=204)