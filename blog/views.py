from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import PostModel


class BlogListView(ListView):
    model = PostModel
    template_name = 'index.html'


class BlogDetailView(DetailView):
    model = PostModel
    template_name = 'detail.html'


class BlogCreateView(CreateView):
    template_name = 'form.html'
    model = PostModel
    fields = '__all__'


class BlogUpdateView(UpdateView):
    template_name = 'update.html'
    model = PostModel
    fields = ['title', 'content']


class BlogDeleteView(DeleteView):
    template_name = 'delete.html'
    model = PostModel
    success_url = reverse_lazy('blog:home')
