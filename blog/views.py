from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils import timezone

def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    if kwargs.get("cat_name"):
        posts = posts.filter(category__name=kwargs["cat_name"])
    if kwargs.get("author_username"):
        posts = posts.filter(author__username=kwargs["author_username"])

    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get("page")
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

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

def blog_search(request):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    if request.method == "GET":
        if s := request.GET.get("s"):
            posts = posts.filter(content__contains=s)
    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)
