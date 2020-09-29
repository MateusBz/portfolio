from datetime import datetime
from django.views.generic import ListView, DetailView, TemplateView

from .models import Post, Category

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
   

class PostDetailView(DetailView):
    model = Post

class AboutMeView(TemplateView):
    template_name = 'blog/about.html' 
