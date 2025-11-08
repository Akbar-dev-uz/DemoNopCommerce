from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request, 'shop/index.html')


def news_archive(request):
    news_list = ["good"]  # News.objects.all()  # пример получения новостей
    return render(request, 'news/archive.html', {'news_list': news_list})
