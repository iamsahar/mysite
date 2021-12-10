from lib2to3.pgen2.literals import simple_escapes
from django import template
from blog.models import Category, Post, Comment

register = template.Library()

@register.simple_tag(name="totalposts")
def function():
    posts = Post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name='comments_count')
def function(pid):
    return Comment.objects.filter(post=pid,approved=True).count()

@register.inclusion_tag("blog/blog-latest-posts.html")
def latestposts(arg=3):
    posts = Post.objects.filter(status=1).order_by("published_date")[:arg]
    return {"posts": posts}

@register.inclusion_tag("blog/blog-post-categories.html")
def postcategories(arg=3):
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {"categories": cat_dict}
