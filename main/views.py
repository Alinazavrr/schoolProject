from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def homePage(request):
    return render(request, 'main/homePage.html')

