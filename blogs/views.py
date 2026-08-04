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
        'categories': categories,
    }
    return render(request, 'category.html', context)