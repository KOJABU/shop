from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddProductForm
from main.models import Catalog


# Create your views here.
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Catalog, id = product_id)
    form = CartAddProductForm(request.POST)
    # print(cart)
    # print(product)
    if form.is_valid():
        cd = form.cleaned_data
        if cd['quantity'] == 0:
            cart.remove(product)
        else:
            cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Catalog, id = product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True })
    return render(request, 'cart/detail.html', {'cart': cart})