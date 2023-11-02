from django.http import HttpResponse
from django.shortcuts import render

from .models import Diets, FavoritesDiets

from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
# Create your views here.

class HomePageView(TemplateView):

    template_name = 'main/homePage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получите объект пользователя из request
        user = self.request.user

        # Добавьте пользователя в контекст
        context['user'] = user

        return context


class DietsView(LoginRequiredMixin, ListView):
    model = Diets
    context_object_name = 'diets'
    template_name = 'main/homePage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class FavoriteView(LoginRequiredMixin, ListView):
