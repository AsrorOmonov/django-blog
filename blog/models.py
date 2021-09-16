from django.db import models
from django.urls import reverse


class PostModel(models.Model):
    title = models.CharField(max_length=32)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
