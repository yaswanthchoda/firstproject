from django.shortcuts import render,redirect,HttpResponse
from firstapp.models import *
from django.core import serializers
import json

# Create your views here.

def home(request):
	print Data.objects.all()
	# request.session['username'] = 'test'
	# print request.session['username']
	return render(request,'home.html',{})

def add(request):
	print request.POST,"uppppppppppp"
	# print request.session['username'],"jjjjjjjjjjjjjjjjjj"
	# print request.POST['name'],request.POST['address']
	# var = Data(name=request.POST['name'],address=request.POST['address'])
	# var = Data(name="s1th",address="hyd")
	# var.save()
	# print var,"jk"
	# v = serializers.serialize('json',var)
	v = {'status':'success'}

	return HttpResponse(json.dumps(v),content_type='application/json')
