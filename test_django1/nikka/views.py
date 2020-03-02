from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def first_name(request):
    return HttpResponse("Nikunj...")


def last_name(request):
    return HttpResponse("Joshi...")
