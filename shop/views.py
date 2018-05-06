# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from shop.models import Product
from shop.forms import ProductForm

# Create your views here.
def home(request):
 # return HttpResponse('Hello World!')
 	queryset = Product.objects.all()
 	context_dict = {'product':queryset}

	return render(request,'home.html',context_dict)

def show_product(request):
	if request.method == 'POST':
		forms = ProductForm(request.POST,request.FILES)
		print request.POST
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/')
	else:
		forms = ProductForm()
	context_dict = {'forms':forms}
	return render (request,'product.html',context_dict)

def update_product(request,pid):
	if request.method=='GET':
		p = Product.objects.get(pk=pid)
		forms = ProductForm(instance=p)
		return render(request,'product_update.html',{'forms':forms})
	else:
		p = Product.objects.get(pk=pid)
		forms = ProductForm(instance=p,data=request.POST)
		if forms.is_valid():
			forms.save()
		return HttpResponseRedirect('/')

def delete_product(request,pid):
	p = Product.objects.get(pk=pid)
	p.delete()
	return HttpResponseRedirect('/')