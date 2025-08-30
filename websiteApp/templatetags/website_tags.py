from django import template
from blog.models import Post
from django.utils import timezone

register = template.Library()



@register.inclusion_tag('websiteApp/recentposts.html')
def recentposts():
    posts = Post.objects.filter(status=1, published__lte=timezone.now()).order_by('-published')[:6]
    return {'posts': posts}