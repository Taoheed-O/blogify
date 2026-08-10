from django.urls import path
from . import views



urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('categories/', views.category_dashboard, name='category_dashboard'),
    path('add_category', views.add_new_category, name='add_category'),
]