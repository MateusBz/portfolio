from datetime import datetime
from django.views.generic import ListView, DetailView

from .models import Post, Category

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
   

class PostDetailView(DetailView):
    model = Post
    
