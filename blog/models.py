from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Свторює табличку в БД з ім'ям News
class News(models.Model):
    # Створює поля з назвою в таблиці (unique=True не дає створювати однакові назви)
    title = models.CharField('Назва статті', max_length=100, default='', unique=True)

    # Створює текстове поле в таблиці
    text = models.TextField('Основний текст статті')

    # Створює поле дати і часу в таблиці (default=timezone.now встанавлює поточний час)
    date = models.DateTimeField('Дата', default=timezone.now)

    # Зв'язує поле автор із таблицeю User (on_delete вказує що робити зі статтями користувача при видалині його)
    # verbose_name='Автор' = Ім'я поля в таблиці
    avtor = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)

    # Поле для цілих чисел
    views = models.IntegerField('Перегляди', default=1)

    # Переадресовує користувача після публікації поста
    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})
    
    # Змінює назву поля в таблиці (така як і назва title)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новину'
        verbose_name_plural = 'Новини'