from django.shortcuts import render,render_to_response,HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context

def homepage(request):
    return render(request, 'homepage.html')

def Register(request):
    return render(request, 'Register.html')