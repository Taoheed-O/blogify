from django.urls import path
from . import views



urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('categories/', views.category_dashboard, name='category_dashboard'),
    path('categories/add/', views.add_new_category, name='add_new_category'),
    path('categories/edit/<int:pk>', views.edit_category, name='edit_category'),
    path('categories/delete/<int:pk>', views.delete_category, name='delete_category'),
    path('posts/', views.posts, name='posts'),
    path('posts/add/', views.add_new_post, name='add_new_post'),
    path('posts/edit/<int:pk>', views.edit_post, name='edit_post'),
    path('posts/delete/<int:pk>', views.delete_post, name='delete_post'),
]