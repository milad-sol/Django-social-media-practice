from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from .models import Post


# Create your views here.

class HomeView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'home/index.html', {'posts': posts})


class PostDetailView(LoginRequiredMixin, View):
    def get(self, request, pk, slug):
        post = Post.objects.get(pk=pk, slug=slug)
        return render(request, 'home/detail.html', {'post': post})
