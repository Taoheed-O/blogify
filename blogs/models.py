from django.db import models

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

