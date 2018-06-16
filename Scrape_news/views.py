# Create your views here.
# URL : menu view: kitchen template: food
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from Scrape_news.models import NewsBbc


def index(request):
    return render(request, "Scrape_news/index.html", {})


def search_form(request):
    return render(request, "Scrape_news/search_form.html", {})


def news_visual(request):
    return render(request, "Scrape_news/News_Visual.html", {})


def search(request):
    if 'publisher' in request.GET and request.GET['publisher']:
        publisher = request.GET['publisher']
        news = NewsBbc.objects.filter(name__icontains=publisher)
        return render(request, "Scrape_news/search_result.html", {'news': news, 'query': publisher})
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)


def post_detail(request, pk):
    post = get_object_or_404(NewsBbc, pk=pk)
    return render(request, 'Scrape_news/post_detail.html', {'post': post})
# About


def about(request):
    return render(request, "Scrape_news/about.html", {})




