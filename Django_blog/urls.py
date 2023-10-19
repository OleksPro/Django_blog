from django.contrib import admin
from django.urls import path, include
from users import views as usersViews
from django.contrib.auth import views as authViews

urlpatterns = [
    path('admin/', admin.site.urls),
    # При переході на головну сторінку піключаємо файл (blog.urls.py)
    path('', include('blog.urls')),
    # Сторінка регістрації (users.views.register)
    path('registration/', usersViews.register, name='registration'),
    path('profile/', usersViews.profile, name='profile'),
    # Використовуємо вбудовані класси django
    path('user/',authViews.LoginView.as_view(template_name='users/user.html') , name='user'),
    path('exit/',authViews.LogoutView.as_view(template_name='users/exit.html') , name='exit'),
    
]
