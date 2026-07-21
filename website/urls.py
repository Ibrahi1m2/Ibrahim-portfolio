from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index-2/', views.index, name='index-2'),
    path('index-3/', views.index, name='index-3'),
    path ('404/', views.page_not_found, name='page_not_found'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('news/', views.news, name='news'),
    path('service/', views.service, name='service'),
    path('service-details/', views.service_details, name='service_details'),

    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio-details/', views.portfolio_details, name='portfolio_details'),

    path('news/', views.news, name='news'),
    path('news-classic/', views.news_classic, name='news_classic'),
    path('news-details/', views.news_details, name='news_details'),
]