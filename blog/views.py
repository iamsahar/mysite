from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils import timezone
from blog.forms import CommentForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect

def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    if kwargs.get("cat_name"):
        posts = posts.filter(category__name=kwargs["cat_name"])
    if kwargs.get("author_username"):
        posts = posts.filter(author__username=kwargs["author_username"])
    if kwargs.get("tag_name"):
        posts = posts.filter(tags__name__in=[kwargs["tag_name"]])

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
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment is submitted successfully.')
        else:
            messages.add_message(request, messages.ERROR, 'Your comment is not submitted.')

    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, id=pid)
    post.counted_views= post.counted_views + 1
    post.save()

    # None if there's no previous
    previous_post = posts.filter(id__lt=post.id).order_by('-id').first()
    # None if there's no next
    next_post = posts.filter(id__gt=post.id).order_by('id').first()

    if not post.login_require:
        comments = Comment.objects.filter(post=post.id, approved=True)
        form = CommentForm()
        context = {"post": post, "comments":comments, "form":form, "previous_post":previous_post, "next_post":next_post}
        return render(request, "blog/blog-single.html", context)
    else:
        return HttpResponseRedirect(reverse('accounts:login'))

def blog_search(request):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    if request.method == "GET":
        if s := request.GET.get("s"):
            posts = posts.filter(content__contains=s)
    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)

def handler404(request, exception):
    return render(request, '404.html', status=404)
