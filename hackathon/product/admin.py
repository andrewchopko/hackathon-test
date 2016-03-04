from django.contrib import admin

# Register your models here.
from .models import Product

class ProductModelAdmin(admin.ModelAdmin):
	list_display = ["title", "created", "updated"]
	list_display_links = ["title"]
	class Meta:
		model = Product

admin.site.register(Product, ProductModelAdmin)