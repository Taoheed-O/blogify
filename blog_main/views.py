from django.shortcuts import render, redirect
from django.http import HttpResponse
from blogs.models import Category, Blog
from about.models import About
from .forms import RegistrationForm


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
    # Get About Us
    about = About.objects.get()

    context = {
        'featured_posts': featured_posts,
        'not_featured_posts': not_featured_posts,
        'about': about,
    }
    return render(request, 'home.html', context=context)


# Registration page
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return redirect('register')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'register.html', context=context)


# Login page
def login(request):
    return render(request, 'login.html')