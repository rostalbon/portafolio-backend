from django.urls import path
from .views import ProjectView, ProjectDetailView

urlpatterns = [
    path('projects/', ProjectView.as_view()),
    path('projects/<int:pk>/', ProjectDetailView.as_view())
]