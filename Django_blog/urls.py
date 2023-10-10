from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # При переході на головну сторінку піключаємо файл blog.urls.py
    path('', include('blog.urls')),
]
