from django.contrib import admin
from django.urls import path, include
from users import views as usersViews
from django.contrib.auth import views as authViews
from django.conf import settings
from django.conf.urls.static import static

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

    # Відновлення паролю
    path('password_reset_complite/',authViews.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_complite.html'), 
        name='password_reset_complite'), 

    path('password_reset/',authViews.PasswordResetView.as_view(
        template_name='users/password_reset.html'), 
        name='password_reset'), 

    path('password_reset_confirm/<uidb64>/<token>/', 
        authViews.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), 
        name='password_reset_confirm'),

    path('password_reset_done/', 
        authViews.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), 
        name='password_reset_done')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)