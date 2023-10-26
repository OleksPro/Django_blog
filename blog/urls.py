from django.urls import path
from . import views

urlpatterns = [
    # Відстежує перехід на головну сторінку в середині додатка blog звертаємось 
    # до файла blog.views.py i звертаємось до метода home
    path('', views.ShowNewsView.as_view(), name='home'),
    # Відстежує динамічну сторінку
    path('user/<str:username>', views.UserAllNewsView.as_view(), name='user-news'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/<int:pk>/update', views.UpdateNewsView.as_view(), name='news-update'),
    path('news/<int:pk>/delete', views.DeleteNewsView.as_view(), name='news-delete'),
    path('news/add', views.CreateNewsView.as_view(), name='news-add'),
    path('contacts', views.contacts, name='contacts')
]