from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rainforest.models import Product
from rainforest.forms import ProductForm


def homepage(request):
    context = {'products': Product.objects.all()}
    response = render(request, 'index.html', context)
    return HttpResponse(response)


def productpage(request, id):
    product = Product.objects.get(pk=id)
    context = {'product': product}
    response = render(request, 'product.html', context)
    return HttpResponse(response)


def root(request):
    return HttpResponseRedirect('home')

def new_product(request):
    new_form = ProductForm()
    context = {'form': new_form}
    response = render(request, 'newproduct.html', context)
    return HttpResponse(response)
