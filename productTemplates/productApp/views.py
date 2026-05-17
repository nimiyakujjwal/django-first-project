from django.shortcuts import render

# Create your views here.
def electronics(request):
    product_dict = {
        'product1': 'Laptop',
        'product2': 'Smartphone',
        'product3': 'Tablet'
    }
    return render(request, 'productApp/products.html', context=product_dict)

def toys(request):
    product_dict = {
        'product1': 'Toy Car',
        'product2': 'Doll',
        'product3': 'Puzzle'
    }
    return render(request, 'productApp/products.html', context=product_dict)

def shoes(request):
    product_dict = {
        'product1': 'Sneakers',
        'product2': 'Boots',
        'product3': 'Sandals'
    }
    return render(request, 'productApp/products.html', context=product_dict)

def index(request):
    return render(request, 'productApp/index.html')
