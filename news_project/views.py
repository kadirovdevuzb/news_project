from django.shortcuts import render, get_object_or_404
from .models import Category, News

def all_news(request):
    news = News.objects.all()
    context = {
        'news': news
    }

    return render(request, 'news/all_news.html', context)

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    context = {
        'news_detail': news
    }
    
    return render(request, 'news/news_detail.html', context)