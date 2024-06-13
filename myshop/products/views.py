from django.shortcuts import render, get_object_or_404
from .models import Category, Product, SubCategory

# Create your views here.

def home(request):
    categories = Category.objects.all()
    return render(request, 'products/home.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    subcategories = category.subcategories.all()
    return render(request, 'products/category_detail.html', {'category': category, 'subcategories': subcategories})

def subcategory_detail(request, subcategory_id):
    subcategory = get_object_or_404(SubCategory, id=subcategory_id)
    products = subcategory.products.all()
    return render(request, 'products/subcategory_detail.html', {'subcategory': subcategory, 'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.view_count += 1
    product.save()
    return render(request, 'products/product_detail.html', {'product': product})