from django.urls import path
from . import views

urlpatterns = [
    # Відстежує перехід на головну сторінку в середині додатка blog звертаємось 
    # до файла blog.views.py i звертаємось до метода home
    path('', views.home, name='home'),
    path('contacts', views.contacts, name='contacts')
]