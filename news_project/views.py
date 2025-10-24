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

    latest_news = News.objects.all().order_by("-published_at")[:6]

    uzb_news_last = News.objects.select_related("category").filter(status=News.Status.Published, category__name__iexact ="o'zbekiston")[0]
    uzb_news = News.objects.select_related("category").filter(status=News.Status.Published, category__name__iexact = "o'zbekiston")[1:5]

    jahon_news_last = News.objects.select_related("category").filter(status=News.Status.Published, category__name__iexact = "jahon")[0]
    jahon_news = News.objects.select_related("category").filter(status=News.Status.Published, category__name__iexact = "jahon")[1:5]

    tech_news_last = News.objects.select_related("category").filter(status=News.Status.Published, category__name__iexact = "texnologiya")[0]
    tech_news = News.objects.select_related("category").filter(status=News.Status.Published, category__name__iexact = "texnologiya")[1:5]

    sport_news_last = News.objects.select_related("category").filter(status=News.Status.Published, category__name__iexact = "sport")[0]
    sport_news = News.objects.select_related("category").filter(status=News.Status.Published, category__name__iexact = "sport")[1:5]

    context = {
        'categories': categories,
        'news': news,
        'latest_news': latest_news,
        'uzb_news_last': uzb_news_last,
        'uzb_news': uzb_news,
        'jahon_news_last': jahon_news_last,
        'jahon_news': jahon_news,
        'tech_news_last': tech_news_last,
        'tech_news': tech_news,
        'sport_news_last': sport_news_last,
        'sport_news': sport_news
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

def category_news(request, ct_name):
    ct_news = News.objects.select_related("category").filter(status=News.Status.Published, category__name__iexact=ct_name.lower()).order_by("-published_at")
    
    context = {
        'ct_news': ct_news,
        'ct_name': ct_name
    }

    return render(request, 'news/category_news.html', context)
