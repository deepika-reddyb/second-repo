from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_view1(request):
	s="<h1>"+"This is 1st response "+"</h1>"
	return HttpResponse(s)
