from django.conf.urls import url
from django.contrib import admin
from .views import (
		product_list,
		product_create,
		product_update,
		product_detail,
		product_delete,
	)

urlpatterns = [
    url(r'^$', product_list),
    url(r'^create/$', product_create),
    url(r'^update/$', product_update),
    url(r'^detail/$', product_detail),
    url(r'^delete/$', product_delete),
]