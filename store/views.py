from django.shortcuts import render, get_object_or_404
from .models import Category, SubCategory, Dress
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from .models import CartItem
from django.core.files.base import ContentFile
import requests
from django.conf import settings
from urllib.parse import urljoin

@login_required(login_url='/login/')
def add_to_cart(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            product_name = data.get('product_name')
            price = float(data.get('price'))
            quantity = int(data.get('quantity'))
            total_price = float(data.get('total_price'))
            image_url = data.get('image_url')


            cart_item = CartItem.objects.create(
                user=request.user,
                product_name=product_name,
                product_image=image_url,  # Assuming you're saving path/URL
                price=price,
                quantity=quantity,
                total_price=total_price,
            )

            return JsonResponse({'success': True, 'message': 'Item added to cart'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)


@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Account created successfully.')
        return redirect('login')

    return render(request, 'auth/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # change to your homepage URL name
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')

    return render(request, 'auth/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


def home(request):
    categories = Category.objects.all()
    category_dresses = {}

    for category in categories:
        dresses = Dress.objects.filter(subcategory__category=category).order_by('-id')[:3]  # Newest 3 dresses
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




