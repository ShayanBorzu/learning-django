from django import template
from blog.models import *
from django.utils import timezone

register = template.Library()


@register.simple_tag(name="test")
def test():
    posts = Post.objects.filter(status=1)
    
    return posts

@register.filter
def snippet(text,number=5):
    return text[:number] + "..."

@register.inclusion_tag('blog/popularposts.html')
def popularposts():
    posts =  Post.objects.filter(status=1, published__lte=timezone.now()).order_by('-views', 'published')[:5]
    return {"posts": posts}

@register.inclusion_tag('blog/categories.html')
def categories():
    posts = Post.objects.filter(status=1, published__lte=timezone.now())
    cat = Category.objects.all()
    cat_dict = {}
    for name in cat:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories': cat_dict}

@register.inclusion_tag('blog/search.html')
def search():
    return {}

