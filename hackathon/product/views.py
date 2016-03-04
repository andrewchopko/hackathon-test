from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def product_list(request):
	return render(request, "index.html", {})
	#return HttpResponse("<h1> Hello!! </h1>")

def product_create(request):
	return render(request, "create_product.html", {})
	#return HttpResponse("<h1> Create!! </h1>")

def product_detail(request):
	return render(request, "detail_product.html", {})
	#return HttpResponse("<h1> Detail!! </h1>")

def product_delete(request):
	return render(request, "delete_product.html", {})
	#return HttpResponse("<h1> Delete!! </h1>")

def product_update(request):
	return render(request, "update_product.html", {})
	#return HttpResponse("<h1> Update!! </h1>")