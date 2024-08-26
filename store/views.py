from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Review, Order,SubCategory,Cart
from .forms import ReviewForm, OrderForm
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404
from .forms import CustomUserCreationForm 

def home(request):
    categories = Category.objects.all()
    return render(request, 'store/home.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    subcategories = category.subcategories.all()
    return render(request, 'store/category_detail.html', {'category': category, 'subcategories': subcategories})

def subcategory_detail(request, subcategory_id):
    
    subcategory = get_object_or_404(SubCategory, id=subcategory_id)
    products = Product.objects.filter(subcategory=subcategory)
    return render(request, 'store/subcategory_detail.html', {'subcategory': subcategory, 'products': products})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'store/category_list.html', {'categories': categories})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = product.reviews.all()
    if request.method == 'POST':
        if 'review_submit' in request.POST:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.product = product
                review.user = request.user
                review.save()
                return redirect('product_detail', product_id=product.id)
        elif 'order_submit' in request.POST:
            order_form = OrderForm(request.POST)
            if order_form.is_valid():
                order = order_form.save(commit=False)
                order.product = product
                order.user = request.user
                order.save()
                return redirect('order_list')
    else:
        review_form = ReviewForm()
        order_form = OrderForm()
    return render(request, 'store/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'order_form': order_form,
        'review_form': review_form,
        
    })
@login_required
def review_edit(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user:
        raise Http404("You are not allowed to edit this review.")

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=review.product.id)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'store/review_edit.html', {'form': form, 'review': review})

@login_required
def review_delete(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user:
        raise Http404("You are not allowed to delete this review.")

    if request.method == 'POST':
        review.delete()
        return redirect('product_detail', product_id=review.product.id)

    return render(request, 'store/review_delete.html', {'review': review})

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    for order in orders:
        order.total_price = order.product.price * order.quantity
    return render(request, 'store/order_list.html', {'orders': orders})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login or any other page
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'store/register.html', {'form': form})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart.products.add(product)
        cart.save()
        return redirect('product_detail', product_id=product_id)
    else:
        return redirect('login')
    

def cart_view(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        products = cart.products.all()
        return render(request, 'store/cart.html', {'products': products})
    else:
        return redirect('login') 




