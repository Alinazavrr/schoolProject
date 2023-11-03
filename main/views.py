from django.http import HttpResponse
from django.shortcuts import render

from .models import Diets, FavoritesDiets


from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
# Create your views here.

class HomePageView(TemplateView):

    template_name = 'main/homePage.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     # Получите объект пользователя из request
    #     user = self.request.user
    #
    #     # Добавьте пользователя в контекст
    #     context['user'] = user
    #
    #     return context


class DietsListView(LoginRequiredMixin, ListView):
    model = Diets
    context_object_name = 'diets'
    template_name = 'main/dietsPage.html'
    paginate_by = 5

class DietsDetailView(LoginRequiredMixin, DetailView):
    model = Diets
    context_object_name = 'diet'
    template_name = 'main/dietDetailPage.html'


class FavoritesDietsListView(LoginRequiredMixin, ListView):
    model = FavoritesDiets
    context_object_name = 'favorite'
    template_name = 'main/favoritePage.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['favoriteExisting'] = True if FavoritesDiets.objects.count() > 0 else False

class AccountDetailView(LoginRequiredMixin, TemplateView):

    template_name = 'main/userDetailPage.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Добавьте пользователя в контекст
        context['user'] = user

        return context
