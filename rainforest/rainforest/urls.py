"""rainforest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from rainforest.views import homepage, productpage, root, new_product, create_product, edit_product, update_product, delete_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homepage, name='homepage'),
    path('products/<int:id>', productpage, name='productpage'),
    path('', root),
    path('products/new/', new_product, name="new_product"),
    path('products/', create_product, name="create_product"),
    path('products/<int:id>/edit/', edit_product, name="edit_product"),
    path('products/<int:id>/', update_product, name="update_product"),
    path('products/<int:id>/delete', delete_product, name="delete_product")
]
