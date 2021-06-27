from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def home(request):
	return HttpResponse("<h1>This is my Home page</h1><p>Paragraph</p>")


def data(request,Name):
	return HttpResponse("<h1>"+Name+"</h1>")


def roll(request, Id):
	return HttpResponse("<h2>"+str(Id)+"</h2>")


def details(request, Name, Id):

	return HttpResponse("<h1>"+Name+":"+str(Id)+"</h1>")


def index(request):

	return render(request, "myApp/index.html")