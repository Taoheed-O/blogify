from django import forms
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