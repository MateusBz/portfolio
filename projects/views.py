from django.views.generic import ListView, DetailView
from projects.models import Project

class ProjectListView(ListView):
    model= Project
    context_object_name = 'projects'

    def get_queryset(self):
        return super().get_queryset().order_by('-pk')

class ProjectDetailView(DetailView):
    model = Project