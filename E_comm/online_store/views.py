from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib import messages
from .models import cart, product, category, Order


# Create your views here.

def home(request):
    return render(request, 'home.html')


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def catagori(request):
    return request(request, 'Catagori.html')


def checkout(request):
    return render(request, 'checkout.html')


def confirmation(request):
    return render(request, 'confirmation.html')


def contact(request):
    return render(request, 'contact.html')


def login(request):
    return render(request, 'login.html')


def main(request):
    return render(request, 'main.html')


def single_blog(request):
    return render(request, 'single-blog.html')


def single_prod(request):
    return render(request, 'single-product.html')


def elements(request):
    return render(request, 'elements.html')


def prod_list(request):
    return render(request, 'product_list.html')


def industries(request):
    return render(request, 'industries.html')


class Home(ListView):
    model = product
    template_name = 'house.html'

def send(request):
    s = product(mainimage='E_comm/assets/img/collection2.png', name='modelss')
    s.save()


# Add to cart view

def add_to_cart(request, slug):
    item = get_object_or_404(product, slug=slug)
    print(slug, 'slug')
    order_item, created = cart.objects.get_or_create(item=item, user=request.user)
    print('hi', item, request.user)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        print(order, order_qs[0])
        print('hi too')
        # check if  the order item is in the order
        if order.ordered_items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This is was succesfully updated")
            return render(request, 'cart.html')
        else:
            order.ordered_items.add(order_item)
            messages.info(request, "This add to your cart successfully")
            return render(request, 'cart.html')
    else:
        order = Order.objects.create(
            user=request.user)
        order.ordered_items.add(order_item)
        messages.info(request, "This item was added to ur cart")
        return render(request, 'cart.html')


# Remove item from cart
def remove_from_cart(request, slug):
    item = get_object_or_404(product, slug=slug)
    print(slug, 'slug')
    cart_qs = cart.objects.filter(
        user=request.user,
        item=item
    )
    if cart_qs.exists():
        carts = cart_qs[0]
        # checking the cart quantity
        if carts.quantity > 1:
            carts.quantity -= 1
            carts.save()
        else:
            cart_qs.delete()
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        orders = order_qs[0]
        # check if the ordered item is in the order
        if orders.ordered_items.filter(item__slug=item.slug).exists():
            order_item = cart.objects.filter(
                item=item,
                user=request.user,
            )[0]
            orders.ordered_items.remove(order_item)
            messages.info(request, "Your item removed from cart")
            return render(request,"cart.html")
        else:
            messages.info(request, "This item was not in ur cart")
            return render(request,'cart.html')
    else:
        messages.info(request, "You do not have active order")
        return render(request,'cart.html')
