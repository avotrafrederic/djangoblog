from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.

def index(request):
    data= Article.objects.all().values()
    context = {
        'data':data
    }
    return render(request,"home/index.html",context)

def articles(request):
    data= Article.objects.all().values()
    context = {
        'data':data
    }
    return render(request,"home/article.html",context)

def showArticle(request,id):
    data = Article.objects.get(id = id)
    article = Article.objects.all()
    print(data)
    context = {
        'data' : data,
        'article': article
    }
    return render(request, "home/show.html",context)