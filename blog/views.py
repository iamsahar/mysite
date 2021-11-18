from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from django.utils import timezone

def blog_view(request):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)

def blog_single(request, pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, id=pid)
    post.counted_views= post.counted_views + 1
    post.save()

    # None if there's no previous
    previous_post = posts.filter(id__lt=post.id).order_by('-id').first()
    # None if there's no next
    next_post = posts.filter(id__gt=post.id).order_by('id').first()

    context = {"post": post, "previous_post":previous_post, "next_post":next_post}
    return render(request, "blog/blog-single.html", context)

def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)
 