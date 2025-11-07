from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'shop/categories.html', {'categories': categories})



def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/products.html', {'products': products})



def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'shop/category_products.html', {
        'category': category,
        'products': products
    })
