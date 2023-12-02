from django.shortcuts import render ,HttpResponse, redirect
from .models import *
from .forms import *
from cart.forms import CartAddProductForm, CartNewProductForm

# Create your views here.
def index(request):
    items = Catalog.objects.all()
    cart_product_form = CartNewProductForm
    return render(request, 'main/index.html', {'items':items,
                                                'cart_product_form':cart_product_form})

def expensive(request):
    items = Catalog.objects.filter(price__gte=30000)
    return render(request, 'main/index.html', {'items': items})

def sort_by_category_mouse(request):
    items = Catalog.objects.filter(category = 1)
    return render(request, 'main/index.html', {'items': items})

def sort_by_category_headphones(request):
    items = Catalog.objects.filter(category = 2)
    return render(request, 'main/index.html', {'items': items})

def detail(request, item_id):
    try:
        item = Catalog.objects.get(id=item_id)
        cart_product_form = CartAddProductForm
    except:
        return redirect('/')
    return render(request, 'main/detail.html', {'item':item,
                                                'cart_product_form':cart_product_form})

def detail_sort1(request, item_id):
    try:
        item = Catalog.objects.get(id=item_id)
        cart_product_form = CartAddProductForm
    except:
        return redirect('/')
    return render(request, 'main/detail.html', {'item':item,
                                                'cart_product_form':cart_product_form})

def detail_sort2(request, item_id):
    try:
        item = Catalog.objects.get(id=item_id)
        cart_product_form = CartAddProductForm
    except:
        return redirect('/')
    return render(request, 'main/detail.html', {'item':item,
                                                'cart_product_form':cart_product_form})
def detail_exp(request, item_id):
    try:
        item = Catalog.objects.get(id=item_id)
        cart_product_form = CartAddProductForm
    except:
        return redirect('/')
    return render(request, 'main/detail.html', {'item':item,
                                                'cart_product_form':cart_product_form})

def add_product(request):
    if request.method == "POST":
        # a = ''
        # print(request.POST.get('category'))
        # for i in request.POST.get('category'):
        #     a = i[0]
        #     print(a)
        Catalog(name=request.POST.get('name'),price=request.POST.get('price'), 
                description=request.POST.get('description'),category=Category.objects.get(id=request.POST.get('category'))).save()
    else:
        pass
    add_form = AddProductForm()
    return render(request, 'main/add.html', {'add_form': add_form})




    
    # try:
        # item: object = Catalog.objects.get(id=item_id)
        
    # except:
    #     return HttpResponse('error')
    #category=Category.objects.get(name=(request.POST.get('category')