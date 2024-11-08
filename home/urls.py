from django.urls import path

from home import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('post/<int:pk>/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
]
