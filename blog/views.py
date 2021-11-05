from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
import datetime

def blog_view(request):
    posts = Post.objects.filter(published_date__lte=datetime.date.today())
    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)

def blog_single(request, pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, id=pid)
    post.counted_views= post.counted_views + 1
    post.save()
    context = {"post": post}
    return render(request, "blog/blog-single.html", context)
