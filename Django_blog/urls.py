from django.contrib import admin
from django.urls import path, include
from users import views as usersViews

urlpatterns = [
    path('admin/', admin.site.urls),
    # При переході на головну сторінку піключаємо файл (blog.urls.py)
    path('', include('blog.urls')),
    # Сторінка регістрації (users.views.register)
    path('registration', usersViews.register, name='registration')
]
