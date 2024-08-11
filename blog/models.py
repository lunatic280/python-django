from django.db import models

class Blog(models.Model):
    title = models.CharField("블로그 제목", max_length=100)
    content = models.TextField("블로그 내용")

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField("댓글 내용")

    def __str__(self):
        return f"{self.blog.title}의 댓글 (ID: {self.id}"