from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Post, Category
from django.utils import timezone
from django.http import Http404, HttpResponse, HttpResponseRedirect
from blog.form import NameForm, BlogContact
from websiteApp.form import NewsLetterForm




# Create your views here.
def blog_index(request, cat_name=None, author=None):
    posts = Post.objects.filter(status=1, published__lte=timezone.now())
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    elif author:
        posts = posts.filter(author__username=author)

    posts = Paginator(posts, 1)
    try:  
        page = int(request.GET.get('p', 1))
        posts = posts.page(page)
    except (EmptyPage, ValueError, PageNotAnInteger):
        raise Http404("Page not found")
        
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

def test_view(request):
    
    if request.method == 'POST':
        form = BlogContact(request.POST)
        if form.is_valid():
            form.save()        
            return HttpResponse('K200')
        else:
            print(form.errors)
     
    form = BlogContact()

    return render(request,'blog/test.html', {'form': form})



def blog_search(request):
    query = request.GET.get('s')
    posts = Post.objects.filter(status=1, published__lte=timezone.now())
    if query:
        posts = (posts.filter(title__icontains=query) | posts.filter(content__icontains=query)).distinct()
    return render(request, 'blog/blog_index.html', {'posts': posts, 'search_query': query})