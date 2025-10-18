from django.shortcuts import render, get_object_or_404
from .models import Category, News
from .forms import ContactForm
from django.http import HttpResponse
def all_news(request):
    news = News.objects.all()
    context = {
        'news': news,
        'categories': categories,
    }

    return render(request, 'news/all_news.html', context)

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    categories = Category.objects.all()
    context = {
        'news_detail': news,
        'categories': categories,
    }
    
    return render(request, 'news/news_detail.html', context)

def home_page_view(request):
    categories = Category.objects.all()
    news = News.objects.all()
    context = {
        'categories': categories,
        'news': news
    }
    return render(request, 'news/index.html', context)

def contact_view(request):
    form = ContactForm(request.POST or None)
    categories = Category.objects.all()
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("Xabaringiz adminsitratsiyaga muvaffaqiyatli yuborildi <a href=''>ASOSIY SAHIFA</a>")
    context = {
        'form': form,
        'categories': categories,
    }
    return render(request, 'news/contact.html', context)

def about_view(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'news': news,
    }
    return render(request, 'news/about.html', context)

def for_base_html(request):
    categories = Category.objects.all()
    news = News.objects.all()
    context = {
        'categories': categories,
        'news': news,
    }
    return render(request, 'news/base.html', context)