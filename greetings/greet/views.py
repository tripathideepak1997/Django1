from django.shortcuts import render,HttpResponse
from datetime import datetime

# Create your views here.

def greetingsWelcome(request):
	if datetime.now().hour > 12 :
		return HttpResponse("Good AfterNoon")
	else :
		return HttpResponse("Good Morning")
