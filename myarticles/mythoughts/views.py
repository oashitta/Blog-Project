from django.shortcuts import render
from .models import Articles

def home(request):
    article = Articles.objects.all()

    return render(request, 'mythoughts/home.html', {'all_articles' : article})

def last_post(request):
    last_article = Articles.objects.last()
    return render(request, 'mythoughts/lastpost.html', {'article': last_article})
