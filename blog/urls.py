from django.urls import path

from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = 'blog'

urlpatterns = [
    path('post/new/', BlogCreateView.as_view(), name='post-new'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/update/', BlogUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post-detail'),
    path('', BlogListView.as_view(), name='home'),
]
