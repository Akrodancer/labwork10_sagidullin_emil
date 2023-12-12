from django.shortcuts import render, redirect, get_object_or_404
from shop_app.models import Product, Category
from django.http import HttpResponseRedirect
from shop_app.forms import ProductForm, CategoryForm
from django.db.models import Q

# Create your views here.
def products_view(request):
    products = Product.objects.all().filter(~Q(remainder=0)).order_by('name')
    return render(request, 'index.html', {'products': products})

def product_view(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'detailed.html', {'product': product})

def category_add_view(request):
    if request.method == 'GET':
        return render(request, 'create_category.html')
    elif request.method == 'POST':
        Category.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )
        return redirect('index')

def product_add_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'create_product.html', {'form': form})
    elif request.method == 'POST':
        form = ProductForm(date=request.POST)
        if form.is_valid():
            product = Product.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                date=form.cleaned_data['date'],
                price=form.cleaned_data['price'],
                product_category_id=form.cleaned_data['product_category_id'],
                image=form.cleaned_data['image']
            )
            return redirect('detailed', pk=product.pk)
        else:
            return render(request, 'create_product.html', {'form': form})

def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(initial={
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'product_category': product.product_category,
            'image': product.image
        })
        return render(request, 'update_product.html', context={'product': product, 'form': form})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.product_category = form.cleaned_data['product_category']
            product.image = form.cleaned_data['image']

            product.save()
            return redirect('detailed', pk=product.pk)

        else:
            return render(request, 'update_product.html', context={'form': form, 'product': product})


def delete_view(request, pk):

    product = get_object_or_404(Product, pk=pk)

    if request.method == 'GET':
        return render(request, 'delete.html', context={'object': product})
    elif request.method == 'POST':
        product.delete()
        return redirect('index')
