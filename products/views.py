from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return render(request, 'products/index.html')

def about(request):
    return render(request, 'products/about.html')


def categories(request, catid):
    return HttpResponse(f"<h1>Категория товара</h1><p>{catid}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена.</h1>")
