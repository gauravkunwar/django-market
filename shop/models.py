# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Database commands here.

class Product (models.Model):
	# name, price and category and image
	name = models.CharField(max_length=100)
	category = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=8,decimal_places=2)
	image = models.ImageField(upload_to='product/%Y/%m/%d')

	def __str__(self):
		return self.name