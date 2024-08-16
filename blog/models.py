from django.db import models
from django.utils import timezone
from django.conf import settings

class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField("약속 내용")
    space = models.CharField(max_length=100, default='default_value')
    meet_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField("댓글 내용")

    def __str__(self):
        return f"{self.blog.title}의 댓글 (ID: {self.id}"