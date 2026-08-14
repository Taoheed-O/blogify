from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog, Category, Comments


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
    # Add comment
    if request.method == 'POST':
        comment = Comments()
        comment.user = request.user
        comment.blog = blog_page
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)

    # Comments
    comments = Comments.objects.filter(blog=blog_page)
    comment_count = comments.count()
    context = {
        'blog_page': blog_page,
        'comments': comments,
        'comment_count': comment_count,
    }
    return render(request, 'blogs.html', context)


# Search blogs view function
def search_blogs(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(body__icontains=keyword), status='Published')
    context = {'blogs': blogs}
    return render(request, 'search_blogs.html', context=context)


# # Search Users view function
# def search_users(request):
#     keyword = request.GET.get('keyword')
#     blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(body__icontains=keyword), status='Published')
#     context = {'blogs': blogs}
#     return render(request, 'search_blogs.html', context=context)


