from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Blog categories...
class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # change the plural on admin site...
    class Meta:
        verbose_name_plural = 'Categories'

    # change the name(admin) to the category title
    def __str__(self):
        return self.title


# Status choices
STATUS_CHOICES = (
("Draft", 'Draft'),
("Published", 'Published'),
)

# Blog information
class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description = models.TextField()
    body = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Draft")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # Return the blog title
    def __str__(self):
        return self.title


# Comments section
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # Verbose name change
    class Meta:
        verbose_name_plural = 'Comments'


    # Return the string comment
    def __str__(self):
        return self.comment
