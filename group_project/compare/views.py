from django.shortcuts import render
from .models import Post, Datasets


def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'compare/home.html', context)


def about(request):
    return render(request, 'compare/about.html', {'title': 'Code'})


def datasets(request):
	context = {
		'datasets': Datasets.objects.all()
	}
	return render(request, 'compare/datasets.html', context)


def information(request):
    return render(request, 'compare/information.html', {'title': 'Dataset Information'})

