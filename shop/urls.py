from django.contrib import admin
from django.urls import path

from shop import views

urlpatterns = [
    path('', views.index, name='products'),
    path('detail/<int:pk>/', views.product_detail, name='product_detail'),
    path('add_comment/<int:pk>/', views.add_comment, name='add_comment'),
]
