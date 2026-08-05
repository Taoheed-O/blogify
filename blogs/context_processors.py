from .models import Category

# Get all categories and return the dict...
def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)
