from django.shortcuts import render
from django.http import HttpResponse

from currency.utils import generate_password as gp

from currency.utils import hello_world as hw

def generate_password(request):
    password = gp()
    return HttpResponse(password)

def hello_world(request):
    hello = hw()
    return HttpResponse(hello)



