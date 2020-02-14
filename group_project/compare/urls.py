from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='compare-home'),
    path('about/', views.about, name='compare-about'),
    path('datasets/', views.datasets, name='compare-datasets'),
    path('information/', views.information, name='compare-information'),
]