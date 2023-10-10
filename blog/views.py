from django.shortcuts import render
from .models import News

def home(request):
    date = {
        # Отримує всі записи із таблиці (Models.News ст.6)
        'news': News.objects.all(),
        # Назва яка передається в HTML
        'title': 'Головна сторінка'
    }

    return render(request, 'blog/home.html', date)


def contacts(request):
    return render(request, 'blog/contacts.html', {'title': 'Сторінка контактів'})