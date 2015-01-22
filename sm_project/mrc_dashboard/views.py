from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<!doctype html><html><head><title>Dashboard</title></head></html>')

# Create your views here.
