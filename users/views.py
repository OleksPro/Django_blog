from django.shortcuts import render, redirect
# Класс для створення форм
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
# Класс для виводу сповіщення
from django.contrib import messages

# Створюємо перехід на сторінку реєстрації
def register(request):
    # Метод передачі даних (передає дані із форм)
    if request.method == 'POST':
        # В об'єкті form зберігаються дані отримані із форми
        form = UserRegisterForm(request.POST)
        # Валідація даних із форм
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # Виводить сповіщення про успішну реєстрації
            messages.success(request, f'Користувач {username} був успішно створений!')
            # Після успішної реєстрації переходить на головну сторінку
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(
        request,
        'users/registration.html',
        {
            'title': 'Сторінка регістрації',
            'form': form
        }
    )