from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Category, Blog



# Homepage...
def home(request):
    # All categories
    # categories = Category.objects.all() # Using the custom context processor instead...
    # Featured posts
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at')
    # Not Featured posts
    not_featured_posts = Blog.objects.filter(is_featured=False, status='Published').order_by('-updated_at')
    # Posts
    posts = Blog.objects.filter(is_featured=False, status='Published')

    context = {
        'featured_posts': featured_posts,
        'not_featured_posts': not_featured_posts,
    }
    return render(request, 'home.html', context=context)