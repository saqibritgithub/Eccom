from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='store/login.html'), name='login'),
    path('home/', views.home, name='home'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('subcategory/<int:subcategory_id>/', views.subcategory_detail, name='subcategory_detail'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('orders/', views.order_list, name='order_list'),
    path('register/', views.register, name='register'),
    path('categories/', views.category_list, name='category_list'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('review/<int:review_id>/edit/', views.review_edit, name='review_edit'),
    path('review/<int:review_id>/delete/', views.review_delete, name='review_delete'),
    
]
