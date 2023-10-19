from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from .forms import BlogPost,Form
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

def search(request):
    keyword = ""
    context = {}
    if request.method == "POST":
        keyword = request.POST.get("search")
        data = Article.objects.filter(title=keyword)
        context = {
            "data":data
        }
    return render(request,'home/article.html',context)

def addArticle(request):
    form = Form()
    context ={'form':form}
    return render(request,"home/add.html",context)

def store(request):
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    return redirect("/")