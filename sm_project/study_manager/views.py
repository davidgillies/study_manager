from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("""<!doctype html><html><head><title>Fenland</title></head>
    </html>""")
