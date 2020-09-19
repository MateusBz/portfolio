from django.views.generic import ListView, DetailView
from projects.models import Project

class ProjectListView(ListView):
    model= Project
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project