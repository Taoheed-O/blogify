from multiprocessing import context
from django.template.defaultfilters import slugify
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from blogs.models import Blog, Category
from .forms import CategoryForm, BlogForm, UserForm, EditUserForm


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


# Show the category dashboard...
def category_dashboard(request):
    return render(request,'dashboards/category_dashboard.html')


# Add new category
def add_new_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_dashboard')
    form = CategoryForm()
    context = {'form': form}
    return render(request,'dashboards/add_new_category.html', context=context)


# Edit existing categories
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_dashboard')
    form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category
    }
    return render(request,'dashboards/edit_category.html', context)


# Delete a category
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('category_dashboard')
    return render(request,'dashboards/category_dashboard.html', context=context)


# View posts
def posts(request):
    blogs = Blog.objects.all()

    context = {
        "blogs": blogs,
    }
    return render(request,'dashboards/posts.html', context=context)


# Add a new post
def add_new_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            slug = form.cleaned_data["title"]
            post.slug = slugify(slug) +'-'+ str(post.id)
            post.save()
            return redirect('posts')
    form = BlogForm()
    context = {'form': form}
    return render(request,'dashboards/add_new_post.html', context=context)


# Edit existing posts
def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            slug = form.cleaned_data["title"]
            post.slug = slugify(slug) + '-' + str(post.id)
            post.save()
            return redirect('posts')
    form = BlogForm(instance=post)
    context = {
        'form': form,
        'post': post
    }
    return render(request,'dashboards/edit_post.html', context)


# Delete post
def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts')


# User section
def users(request):
    users = User.objects.all()
    context = {
        'users': users
               }
    return render(request, 'dashboards/users.html', context)


# Add new user
def add_new_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print(form.errors)
    form = UserForm()
    context = {'form': form}
    return render(request,'dashboards/add_new_user.html', context=context)


# Edit user
def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    form =  EditUserForm(instance=user)
    context = {
        'form': form,
        'user': user
    }
    return render(request, 'dashboards/edit_user.html', context)


# Delete user
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('users')