from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

menu = ["О сайте","Добавить статью","Обратная связь","Войти"]


def index(request):
    return render(request, 'products/index.html',{'menu': menu, 'title':'Главная страница'})

def about(request):
    return render(request, 'products/about.html',{'title':'О сайте'})


def categories(request, catid):
    return HttpResponse(f"<h1>Категория товара</h1><p>{catid}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена.</h1>")
