from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
# Create your views here.
def product_list(request):
	queryset = Product.objects.all()
	context = {
		"object_list": queryset,
	}
	return render(request, "index.html", context)
	#return HttpResponse("<h1> Hello!! </h1>")

def product_create(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully Added New Product")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "create_product.html", context)
	#return HttpResponse("<h1> Create!! </h1>")

def product_detail(request, id):
	instance = get_object_or_404(Product, id=id)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "detail_product.html", context)
	#return HttpResponse("<h1> Detail!! </h1>")

def product_delete(request, id=None):
	instance = get_object_or_404(Product, id=id)
	instance.delete()
	messages.success(request, "Successfully Deleted")
	return redirect("products:list")

def product_update(request, id=None):
	instance = get_object_or_404(Product, id=id)
	
	form = ProductForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Product Updated")
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form": form
	}
	return render(request, "create_product.html", context)
	#return HttpResponse("<h1> Update!! </h1>")