from django.shortcuts import render,HttpResponse
from django.views import View
# Create your views here.

class HomeView(View):
    def get(self, request):
        return  HttpResponse("<h1>Hello World!</h1>")