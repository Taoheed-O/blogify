from django.db import models

# Create your models here.

class About(models.Model):
    about_heading = models.CharField(max_length=200)
    about_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)