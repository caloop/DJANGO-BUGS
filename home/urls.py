from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('portifolio/', views.portifolio),
    path('artes/', views.sobre),

]
