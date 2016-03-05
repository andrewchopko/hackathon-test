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
    url(r'^$', product_list, name='list'),
    url(r'^create/$', product_create),
    url(r'^(?P<id>\d+)/edit/$', product_update, name='edit'),
    url(r'^(?P<id>\d+)$', product_detail, name='detail'),
    url(r'^(?P<id>\d+)/delete/$', product_delete),
]