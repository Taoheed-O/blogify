from .models import Category, Blog
from about.models import SocialLinks
# Get all categories and return the dict...
def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

# def get_related_blogs(request, category):
#     related_blogs = Blog.objects.filter(category=category)
#     return dict(related_blogs=related_blogs)

def get_social_links(request):
    social_links = SocialLinks.objects.all()
    return dict(social_links=social_links)