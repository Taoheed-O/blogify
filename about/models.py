from django.db import models

# Create your models here.

class About(models.Model):
    about_heading = models.CharField(max_length=200)
    about_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # change the plural on admin site...
    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.about_heading


class SocialLinks(models.Model):
    social_platform = models.CharField(max_length=200)
    social_link = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Social Links'

    def __str__(self):
        return self.social_platform