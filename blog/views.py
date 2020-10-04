from datetime import datetime
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404

from .models import Post, Category

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
   

class PostDetailView(DetailView):
    model = Post

class AboutMeView(TemplateView):
    template_name = 'blog/about.html'


class CategoryPostListView(ListView):
    template_name = 'blog/category_list.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, name=self.kwargs['category'])
        return Post.objects.filter(categories=self.category)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

        
    context_object_name = 'posts'