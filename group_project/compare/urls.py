from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='compare-home'),
    path('about/', views.about, name='compare-about'),
    path('code/', views.code, name='compare-code'),
    path('datasets/', views.datasets, name='compare-datasets'),
    path('information/', views.information, name='compare-information'),
    path('myaccount/', views.myaccount, name='compare-myaccount'),
    path('solutions/',views.solutions,name='compare-solutions'),
    path('problems/',views.problems,name="compare-problems"),
    path('favourite/',views.favourite,name='compare-favourite'),
]
