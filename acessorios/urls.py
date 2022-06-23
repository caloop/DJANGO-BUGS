from django.urls import path
from . import views


urlpatterns = [
    path('', views.acessorios),
    path('item', views.item),
]
