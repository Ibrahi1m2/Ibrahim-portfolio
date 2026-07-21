from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    return render(request, 'faq.html')

def service(request):
    return render(request, 'service.html')

def service_details(request):
    return render(request, 'service-details.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def news(request):
    return render(request, 'news.html')

def news_classic(request):
    return render(request, 'news-classic.html')

def news_details(request):
    return render(request, 'news-details.html')     
def page_not_found(request, exception):
    return render(request, '404.html', status=404)