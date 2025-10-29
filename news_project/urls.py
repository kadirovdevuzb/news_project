from django.urls import path
from .views import all_news, news_detail, home_page_view, contact_view, about_view, category_news

urlpatterns = [
    path('all_news/', all_news, name='all_news'),   
    path('all_news/<slug:news>/', news_detail, name='news_detail'),
    path('', home_page_view, name='home_page'),
    path('contact-us/', contact_view, name='contact_us'),
    path('about_us/', about_view, name = 'about_us'),
    path('category_news/<str:ct_name>/', category_news, name='category_news')
]  