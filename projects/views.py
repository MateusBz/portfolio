from django.views.generic import ListView
from projects.models import Project

class ProjectListView(ListView):
    model= Project
