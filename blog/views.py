from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone

# Create your views here.
def blog_index(request):
    posts = Post.objects.filter(status=1, published__lte=timezone.now())
    return render(request, "blog/blog_index.html",{'posts': posts})


def blog_about(request, pk):   
    
    post = get_object_or_404(Post, id=pk, status=1, published__lte=timezone.now())
    # Find previous and next posts
    prev_post = Post.objects.filter(status=1, published__lte=timezone.now(), id__lt=post.id).order_by('-id').first() # type: ignore
    next_post = Post.objects.filter(status=1, published__lte=timezone.now(), id__gt=post.id).order_by('id').first() # type: ignore
    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post,
    }
    post.views += 1
    post.save(update_fields=['views'])
    return render(request, 'blog/blog_about.html', context)
