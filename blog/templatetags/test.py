from django import template
from blog.models import *

register = template.Library()


@register.simple_tag(name="test")
def test():
    posts = Post.objects.filter(status=1)
    
    return posts