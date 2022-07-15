from django.contrib import admin
from django.urls import path, include
from .views import HomeView, ViewProduct,  LikeView
from . import views
urlpatterns = [
    path('', HomeView.as_view(), name="home"), 
    path('Prdouct/<int:pk>', ViewProduct.as_view(), name="product"),
    path('like/<int:pk>', views.LikeView, name="like_post"),
    path('category/<str:cats>/', views.CategoryView, name="category"),
    path('search/', views.search, name="search"),
]