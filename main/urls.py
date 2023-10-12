from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='main_page'),
    path('diets/', views.HomePageView.as_view(), name='diets_page'),
    path('favorites/', views.HomePageView.as_view(), name='favorites_page'),
    path('account/', views.HomePageView.as_view(), name='account_page'),
]