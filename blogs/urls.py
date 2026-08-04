from django.urls import path
from . import views

urlpatterns = [
    path('<int:category_id>', views.categorical_posts, name="categorical_posts"),
]