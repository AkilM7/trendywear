from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('product/<int:dress_id>/', views.single_product, name='single_product'),
    path('contact/', views.contact, name='contact'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),  # ✅ Your own login view
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
]
