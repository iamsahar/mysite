from django.shortcuts import render
from blog.models import Post
from django.utils import timezone
import datetime

def blog_view(request):
    posts = Post.objects.filter(published_date__lte=datetime.date.today())
    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)

def blog_single(request, pid):
    post = Post.objects.get(id=pid)
    post.counted_views= post.counted_views + 1
    post.save()
    context = {"post": post}
    return render(request, "blog/blog-single.html", context)
