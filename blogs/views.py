from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Category
# Create your views here.

# View posts by category
def categorical_posts(request, category_id):
    categories = Category.objects.all()
    posts = Blog.objects.filter(status='Published', category_id=category_id)
    category = Category.objects.get(id=category_id)
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'category.html', context)


# Blog views [detailed view of each blog]
def blogs(request, slug):
    return render(request, 'blogs.html')