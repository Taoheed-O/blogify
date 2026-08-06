from django.shortcuts import render, get_object_or_404, redirect
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
    blog_page = get_object_or_404(Blog, slug=slug, status = 'Published')
    context = {'blog_page': blog_page}
    return render(request, 'blogs.html', context)