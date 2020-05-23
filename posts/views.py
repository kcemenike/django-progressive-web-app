from django.shortcuts import render
from django.core import serializers
from .models import Feed
from django.http import HttpResponse, JsonResponse
import json

# Create your views here.


def index(request):
    template = 'posts/index.html'
    results = Feed.objects.all()
    jsondata = serializers.serialize('json', results)
    context = {
        'results': results,
        'jsondata': jsondata,
    }
    return render(request, template, context)


def getdata(request):
    results = Feed.objects.all()
    jsondata = serializers.serialize('json', results)
    return HttpResponse(jsondata)


def getjson(request):
    results = list(Feed.objects.all().values())
    # jsondata = serializers.serialize('json', results)
    # print(jsondata)
    return JsonResponse(results, safe=False)


def base_layout(request):
    template = 'posts/base.html'
    return render(request, template)
