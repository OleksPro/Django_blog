from django.shortcuts import render
# Імпорт классу для створення форм
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm

# Створюємо перехід на сторінку регістрації
def register(request):
    form = UserRegisterForm()

    return render(
        request,
        'users/registration.html',
        {
            'title': 'Сторінка регістрації',
            'form': form
        }
    )