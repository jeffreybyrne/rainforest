from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from rainforest.models import Product
from rainforest.forms import ProductForm


def homepage(request):
    return render(request, 'index.html', {
        'products': Product.objects.all()
    })


def productpage(request, id):
    return render(request, 'product.html', {
        'product': Product.objects.get(pk=id)
    })


def root(request):
    return HttpResponseRedirect('home')

def new_product(request):
    new_form = ProductForm()
    context = {'form': new_form}
    response = render(request, 'newproduct.html', context)
    return HttpResponse(response)

def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            new_product = form.save()
            return HttpResponseRedirect('/product/' +str(new_product.pk))
        else:
            print(form.errors)
    else:
        form = ProductForm()
    return render(request, 'newproduct.html', {'form': form})

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'editproduct.html', {
        'form': ProductForm(instance=product),
        'id': id
    })

def update_product(request, id):

    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance = product)
        if form.is_valid():
            # import ipdb; ipdb.set_trace()
            product = form.save(commit=False)
            product.name = request.POST['name']
            product.price = request.POST['price']
            product.description = request.POST['description']
            product.save()
            return render(request, 'product.html', {
                'product': product
            })
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/' + str(id) + '/edit/', {'form': form})

# def post_edit_product(request, id):
#     product = get_object_or_404(Product, pk=id)
#     product.name = request.POST['name']
#     product.price = request.POST['price']
#     product.description = request.POST['description']
#     product.save()
#
#
#     product = get_object_or_404(Product, pk=id)
#     new_form = ProductForm(instance=product)
#     context = {'form': new_form}
#     response = render(request, 'editproduct.html', context)
#     return HttpResponse(response)
