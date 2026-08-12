from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from blogs.models import Category, Blog


# Category form
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


# Blog Posts
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'category', 'image', 'short_description', 'body', 'status', 'is_featured')


# User form
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')