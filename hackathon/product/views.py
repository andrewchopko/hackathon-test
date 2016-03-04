from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.
def product_list(request):
	queryset = Product.objects.all()
	context = {
		"object_list": queryset,
	}
	return render(request, "index.html", context)
	#return HttpResponse("<h1> Hello!! </h1>")

def product_create(request):
	return render(request, "create_product.html", {})
	#return HttpResponse("<h1> Create!! </h1>")

def product_detail(request):
	instance = get_object_or_404(Product, id=1)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "detail_product.html", context)
	#return HttpResponse("<h1> Detail!! </h1>")

def product_delete(request):
	return render(request, "delete_product.html", {})
	#return HttpResponse("<h1> Delete!! </h1>")

def product_update(request):
	return render(request, "update_product.html", {})
	#return HttpResponse("<h1> Update!! </h1>")