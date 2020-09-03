from django.urls import path

from .views import home, titulo

urlpatterns = [
    path('home/', home, name='home'),
    path('titulo/', titulo, name='titulo'),
]
