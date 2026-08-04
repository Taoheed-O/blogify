from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Category, Blog



# Homepage...
def home(request):
    # All categories
    categories = Category.objects.all()
    # Featured posts
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at')
    # Posts
    posts = Blog.objects.filter(is_featured=False, status='Published')

    context = {
        'categories': categories,
        'featured_posts': featured_posts
    }
    return render(request, 'home.html', context=context)