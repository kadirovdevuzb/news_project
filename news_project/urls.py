from django.urls import path
from .views import all_news, news_detail

urlpatterns = [
    path('all_news/', all_news, name='all_news'),   
    path('all_news/<int:pk>/', news_detail, name='news_detail')
]  