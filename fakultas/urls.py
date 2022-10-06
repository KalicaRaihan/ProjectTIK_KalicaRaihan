from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('faperta/', views.faperta, name='faperta'),
    path('fh/', views.fh, name='fh'),
    path('fkip/', views.fkip, name='fkip'),
    path('ft/', views.ft, name='ft'),
    path('feb/', views.feb, name='feb'),
    path('fisip/', views.fisip, name='fisip'),
    path('fk/', views.fk, name='fk'),
    path('pascasarjana/', views.pascasarjana, name='pascasarjana'),
]