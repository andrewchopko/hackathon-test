from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)

class Product(models.Model):
	title = models.CharField(max_length=255)
	description = models.CharField(max_length=500)
	content = models.TextField()
	image = models.FileField(upload_to=upload_location,null=True, blank=True)
	price = models.DecimalField(max_digits=4, decimal_places=1, null=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("products:detail", kwargs={"id": self.id})

	class Meta:
		ordering = ["-created", "-updated"]