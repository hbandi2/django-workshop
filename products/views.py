from django.shortcuts import render
from products.models import Product
# from django.http import HttpResponse

# Create your views here.


def product_list(request):
    # query db to return all the products
    products = Product.objects.all()
    print(products)
    return render(request, 'products/product_list.html', {'products': products})


def product_details(request, pk):
    # query db to get given product
    product = Product.objects.get(pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

