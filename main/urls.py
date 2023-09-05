from django.urls import path
from . import views

urlpatterns = [
    path('2', views.homePageView.as_view()),
    path('', views.homePage),

]