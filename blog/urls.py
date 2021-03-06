from django.urls import path

from .views import PostListView, PostDetailView, AboutMeView, CategoryPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('about/', AboutMeView.as_view(), name='about_me'),
    path('<category>/', CategoryPostListView.as_view(), name='post_category'),
]
