"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from base.views import product_views as views

urlpatterns = [
    path('', views.getProducts, name='products'),

    path('create/', views.createProduct, name='product-create'),
    path('upload/', views.uploadImage, name='image-upload'),

    path('<str:pk>/reviews/', views.createProductReview, name='create-review'),
    path('top/', views.getTopProducts, name='top-products'),
    path('<str:pk>/', views.getProduct, name='product'),

    path('delete/<str:pk>/', views.deleteProduct, name='product-delete'),
    path('update/<str:pk>/', views.updateProduct, name='product-update'),
]
