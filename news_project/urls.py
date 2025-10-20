from django.urls import path
from .views import all_news, news_detail, home_page_view, contact_view, about_view

urlpatterns = [
    path('all_news/', all_news, name='all_news'),   
    path('all_news/<int:pk>/', news_detail, name='news_detail'),
    path('', home_page_view, name='home_page'),
    path('contact-us/', contact_view, name='contact_us'),
    path('about_us/', about_view, name = 'about_us'),
]  