from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Person


class PersonBaseView(View):
    model = Person
    fields = ['name', 'age']
    success_url = "/"


class PersonListView(PersonBaseView, ListView):
    """Просмотреть список всех имен. Будем использовать переменную 'person_list' в шаблоне"""
    pass


class PersonCreateView(PersonBaseView, CreateView):
    """Создание новой персоны (Принимаем имя и возраст)"""
    pass


class PersonUpdateView(PersonBaseView, UpdateView):
    """Редактирование созданных записей"""
    pass


class PersonDeleteView(PersonBaseView, DeleteView):
    """Удаление созданной записи"""
    pass
