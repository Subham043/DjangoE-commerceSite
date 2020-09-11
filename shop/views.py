from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product,Contact,Order,Update
from math import ceil
import json

# Create your views here.
def index(request):
	allProds = []
	catprods = Product.objects.values('category','id')
	cats = {item['category'] for item in catprods}
	for cat in cats:
		prod = Product.objects.filter(category = cat)
		n = len(prod)
		nSlides = n // 4 + ceil((n / 4) - (n // 4))
		allProds.append([prod,range(1,nSlides),nSlides])
	context = {'allProds':allProds}
	return render(request, 'shop/index.html',context)

def about(request):
	return render(request,'shop/about.html')

def contact(request):
	if request.method == 'POST':
		name = request.POST.get('name','')
		email = request.POST.get('email','')
		phone = request.POST.get('phone','')
		desc = request.POST.get('desc','')
		contact = Contact(name=name,email=email,phone=phone,desc=desc)
		contact.save()
		contacted = True
		return render(request,'shop/contact.html',{'contacted':contacted})
	return render(request,'shop/contact.html')

def tracker(request):
	if request.method == 'POST':
		orderId = request.POST.get('orderId','')
		email = request.POST.get('email','')
		try:
			order = Order.objects.get(id=orderId,email=email)
			if order:
				update = Update.objects.filter(order_id=orderId)
				updates = []
				for item in update:
					updates.append({'text':item.update_desc,'time':item.timestamp})
					response = json.dumps(updates,default=str)
				return HttpResponse(response)
			else:
				return HttpResponse('{}')
		except Exception as e:
			return HttpResponse('{}')
	return render(request,'shop/tracker.html')

def search(request):
	return render(request,'shop/search.html')

def productView(request,id):
	product = Product.objects.filter(id=id)
	context = {'product':product[0]}
	return render(request,'shop/productView.html',context)

def checkout(request):
	if request.method == 'POST':
		items_json = name = request.POST.get('itemsJson','')
		name = request.POST.get('name','')
		email = request.POST.get('email','')
		phone = request.POST.get('phone','')
		address = request.POST.get('address1','') + " " + request.POST.get('address2','')
		city  = request.POST.get('city','')
		state = request.POST.get('state','')
		zip_code = request.POST.get('zip_code','')
		order = Order(items_json=items_json,name=name,email=email,phone=phone,address=address,city=city,state=state,zip_code=zip_code)
		order.save()
		update = Update(order_id=order.id,update_desc="The order has been placed")
		update.save()
		thank = True
		order_id = order.id
		context = {'thank':thank,'order_id':order_id}
		return render(request,'shop/checkout.html',context)
	return render(request,'shop/checkout.html')