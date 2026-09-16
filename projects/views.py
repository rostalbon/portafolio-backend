from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView as ApiView

from projects.models import ProjectsTable
from projects.serializers import ProjectSerializer

class ProjectView(ApiView):
    # Para usar el GET sólo hay que escribir el endpoint de projects (ejemplo: http://127.0.0.1:8000/api/projects/)
    def get(self, request):
        projects = ProjectsTable.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=200)
    # Para usar el POST hay que ir a Body -> Raw -> JSON y escribir todos los parámetros requeridos para el registro de proyectos como JSON
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class ProjectDetailView(ApiView):
    # Para usar el DELETE hay que escribir el endpoint (ejemplo: http://127.0.0.1:8000/api/projects/1/)
    def delete(self, request, pk):
        try:
            project = ProjectsTable.objects.get(pk=pk)
        except ProjectsTable.DoesNotExist:
            return Response(
                {"error": "Proyecto no encontrado"},
                status=404,
            )
        project.delete()
        return Response(status=204)
    # Para usar el GET que filtra por ID hay que escribir el endpoint (ejemplo: http://127.0.0.1:8000/api/projects/1/)
    def get(self, request, pk):
        try:
            project = ProjectsTable.objects.get(pk=pk)
        except ProjectsTable.DoesNotExist:
            return Response(
                {"error": "Proyecto no encontrado."},
                status=404
            )
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=200)
    # Para usar el PUT en Postman hay que escribir el endpoint (ejemplo: http://127.0.0.1:8000/api/projects/1/) e ir a Body -> Raw -> JSON y escribir todos los parámetros requeridos para el registro de proyecto como JSON
    def put(self, request, pk):
        try:
            project = ProjectsTable.objects.get(pk=pk)
        except ProjectsTable.DoesNotExist:
            return Response(
                {"error": "Proyecto no encontrado."},
                status=404
            )
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)