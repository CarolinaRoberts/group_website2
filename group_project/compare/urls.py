from django.urls import path
from . import views
from .views import ProblemsView, ProblemDetailView

urlpatterns = [
    path('', views.home, name='compare-home'),
    path('about/', views.about, name='compare-about'),
    path('code/', views.code, name='compare-code'),
    path('datasets/', views.datasets, name='compare-datasets'),
    path('information/', views.information, name='compare-information'),
    path('myaccount/', views.myaccount, name='compare-myaccount'),
    path('solutions/',views.solutions,name='compare-solutions'),
    path('myproblems/',views.problems,name="compare-problems"),
    path('favourite/',views.favourite,name='compare-favourite'),
    path('problems/', ProblemsView.as_view(), name='problems'),
    path('problems/<int:pk>/', ProblemDetailView.as_view(), name='problem_detail'),
]
