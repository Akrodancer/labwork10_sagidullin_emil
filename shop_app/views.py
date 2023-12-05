from django.shortcuts import render, redirect
from shop_app.models import Product, Category
from django.http import HttpResponseRedirect

# Create your views here.
def render_index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def render_detailed(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'detailed.html', {'product': product})

def create_category(request):
    if request.method == 'GET':
        return render(request, 'create_category.html')
    elif request.method == 'POST':
        Category.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )
        return redirect('index')

def create_product(request):
    categories = Category.objects.all()
    if request.method == 'GET':
        return render(request, 'create_product.html', {'categories': categories})
    elif request.method == 'POST':
        Category.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            date=request.POST.get('date'),
            price=request.POST.get('price'),
            product_category=request.POST.get('product_category'),
            image=request.POST.get('image')
        )
        return redirect('index')
