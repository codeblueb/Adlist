from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from news.models import Article

def home(request):
    
    site = Main.objects.get(pk=1)
    articles = Article.objects.all()
    context = {
        "news": "News | Home",
        "site": site,
        "articles": articles,
    }
    return render(request, 'front/home.html', context)

def about(request):
    
    context = {
        "about": "News | About"
    }
    return render(request, 'front/about.html', context)
