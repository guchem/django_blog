import imp
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_blogs')
    title = models.CharField(max_length=80)
    content = models.TextField()



class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comments')
    content = models.TextField()

