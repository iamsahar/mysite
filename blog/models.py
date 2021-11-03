from importlib.resources import contents
from turtle import title
from django.db import models

class Post(models.Model):
    # image =
    # author = 
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tags = 
    # category = 
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

