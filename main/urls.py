from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='main_page'),

    path('diets/', views.DietsListView.as_view(), name='diets_page'),
    path('diets/<int:pk>', views.DietsDetailView.as_view(), name='diets_detail'),

    path('favorites/', views.FavoritesDietsListView.as_view(), name='favorites_page'),
    path('account/', views.AccountDetailView.as_view(), name='account_page'),
]