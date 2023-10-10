from django.contrib import admin
# Імпорт таблиці News 
from .models import News

# Регістрація таблиці в панелі адміністратора
admin.site.register(News)
