from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
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
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('home')
    form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'login.html',  context=context)


# Logout
def logout(request):
    auth.logout(request)
    return redirect('home')