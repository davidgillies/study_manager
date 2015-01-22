from django.shortcuts import render
from django.http import HttpResponse
from django.apps import apps
from sm_project.settings import base as settings

# models_list = ','.join([x.__name__ for x in apps.get_models()])
apps_list = ', '.join(settings.MY_APPS)

def index(request):
    return HttpResponse("""<!doctype html><html><head><title>Dashboard</title></head>
    """+apps_list+'</html>')

# Create your views here.
