from django.shortcuts import render, get_object_or_404
from .models import Category, SubCategory, Dress

def home(request):
    categories = Category.objects.all()
    category_dresses = {}

    for category in categories:
        dresses = Dress.objects.filter(subcategory__category=category)
        category_dresses[category] = dresses

    return render(request, 'home.html', {
        'categories': categories,
        'category_dresses': category_dresses
    })


# About page
def about(request):
    return render(request, 'about.html')

# Products page: show categories and their subcategories with dresses
def products(request):
    categories = Category.objects.all()
    category_dresses = {}

    for category in categories:
        dresses = Dress.objects.filter(subcategory__category=category)
        category_dresses[category] = dresses
    
    return render(request, 'products.html', {'categories': categories,
    'category_dresses': category_dresses})


# Single product view by ID
def single_product(request, dress_id):
    dress = get_object_or_404(Dress, id=dress_id)
    return render(request, 'single_product.html', {
        'dress': dress
    })
    
def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    subcategories = SubCategory.objects.filter(category=category)
    dresses = Dress.objects.filter(subcategory__category=category)  

    context = {
        'category': category,
        'subcategories': subcategories,
        'dresses': dresses
    }

    return render(request, 'category_detail.html', context)
# Contact page
def contact(request):
    return render(request, 'contact.html')

