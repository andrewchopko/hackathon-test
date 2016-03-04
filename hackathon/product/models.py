from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=255)
	description = models.CharField(max_length=500)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return title

	def __str__(self):
		return title