from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import News
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView
    )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Вивід статті на головну сторінку
class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    # Сортування статей по даті
    ordering = ['-date']
    # Додає пагінацію
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ShowNewsView, self).get_context_data(**kwargs)
        context['title'] = 'Головна сторінка'
        return context

# Перехід на сторінку зі статтями від одного автора
class UserAllNewsView(ListView):
    model = News
    template_name = 'blog/user_news.html'
    context_object_name = 'news'
    # Додає пагінацію
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(avtor=user).order_by('-date')

    def get_context_data(self, **kwards):
        context = super(UserAllNewsView, self).get_context_data(**kwards)
        context['title'] = f"Cтатті від користувача {self.kwargs.get('username')}"
        return context
    
# Перехід на статтю
class NewsDetailView(DetailView):
    model = News

    def get_context_data(self, **kwards):
        context = super(NewsDetailView, self).get_context_data(**kwards)
        # Додає вивід тайтлу по назві статті
        context['title'] = News.objects.get(pk=self.kwargs['pk'])
        return context

# Додавання статті в БД
class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    template_name = 'blog/create_news.html'
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwards):
        context = super(CreateNewsView, self).get_context_data(**kwards)
        # Додає вивід тайтлу по назві статті
        context['title'] = 'Створення статті'
        context['btn_text'] = 'Створити статтю'
        return context

# Редагування статті
class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'blog/create_news.html'
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)
 
    def get_context_data(self, **kwards):
        context = super(UpdateNewsView, self).get_context_data(**kwards)
        # Додає вивід тайтлу по назві статті
        context['title'] = 'Оновлення статті'
        context['btn_text'] = 'Оновити статтю'
        return context
    
    # Дозволяє редагувати статтю тільки автору даної статті
    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        else:
            return False

# Видалення Статті
class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'
    template_name = 'blog/delete_news.html'

    # st. 68
    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        else:
            return False
    
def contacts(request):
    return render(request, 'blog/contacts.html', {'title': 'Сторінка контактів'})