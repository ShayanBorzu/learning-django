from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone

# Create your views here.
def blog_index(request):
    posts = Post.objects.filter(status=1, published__lte=timezone.now())
    return render(request, "blog/blog_index.html",{'posts': posts})


def blog_about(request, pk):   
    post = get_object_or_404(Post, id=pk) 
    context = {'post': post}
    post.views += 1
    post.save(update_fields=['views'])  # Efficient update
    return render(request, 'blog/blog_about.html', context)

def test(request, pk):
    post = get_object_or_404(Post, id=pk) 
    context = {'post': post}
    return render(request, "blog/test.html", context)