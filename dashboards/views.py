from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blogs.models import Blog, Category

# Create your views here.

# Dashboard
@login_required(login_url='login')
def dashboard(request):
    blog_count = Blog.objects.all().count()
    category_count = Category.objects.all().count()
    featured_count = Blog.objects.filter(is_featured=True).count()
    published_count = Blog.objects.filter(status='Published').count()
    drafted_count = Blog.objects.filter(status='Draft').count()

    context = {
        "blog_count": blog_count,
        "category_count": category_count,
        "featured_count": featured_count,
        "published_count": published_count,
        "drafted_count": drafted_count
    }
    return render(request,'dashboards/dashboard.html', context=context)


def category_dashboard(request):

    return render(request,'dashboards/category_dashboard.html')