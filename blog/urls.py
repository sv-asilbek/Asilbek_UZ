from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('detail/<int:pk>/', article_detail_page, name='detail'),
    path('detail/<int:pk>/', article_detail_page, name='article_detail'),
    path('comment/submit/<int:pk>/', comment_submit_view, name='comment_submit'),
    path('search/', search_results, name='search_results'),
]
