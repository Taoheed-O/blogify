from django.urls import path
from . import views



urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('categories/', views.category_dashboard, name='category_dashboard'),
]