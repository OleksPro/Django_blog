from django.db import models
from django.contrib.auth.models import User

# Створюемо нову таблицю
class Profile(models.Model):
    # Створює зв'язок між двома моделями
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Користувач')
    img = models.ImageField('Фото профілю', default='user_images/default.png', upload_to='user_images')
    
    def __str__(self):
        return f'Профіль користувача {self.user.username}'
    
    class Meta:
        verbose_name = 'Профіль'
        verbose_name_plural = 'Профілі'