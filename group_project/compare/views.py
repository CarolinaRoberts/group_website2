import pymysql
from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render
from utils import sqlhelper
from .models import Problem, Dataset
from .forms import SubmitProbSpecForm
from django.views.generic import TemplateView, ListView, CreateView, DetailView


def home(request):
    context = {
        'posts': Problem.objects.all()
    }
    return render(request, 'compare/home.html', context)

class ProblemsView(ListView):
    template_name = 'compare/problems.html'
    model = Problem
    context_object_name = 'problemsList'

class ProblemDetailView(DetailView):
    model = Problem
    template_name = 'compare/problem_detail.html'

def code(request):
    return render(request, 'compare/code.html', {'title': 'Code'})


def about(request):
	form = SubmitProbSpecForm()
	return render(request, 'compare/about.html', {'form': form})


def datasets(request):
    context = {
        'datasets': Dataset.objects.all()
    }
    return render(request, 'compare/datasets.html', context)


def information(request):
    return render(request, 'compare/information.html', {'title': 'Dataset Information'})


def myaccount(request):
    nid = request.user.id
    username = sqlhelper.get_one("select username from auth_user where id=%s", [nid])
    email = sqlhelper.get_one("select email from auth_user where id=%s", [nid])
    print(username)
    if request.method == 'POST':
        nid = request.POST.get('id')
        opw = request.POST.get('Opwd')
        npw = request.POST.get('Npwd')
        cpw = request.POST.get('Cpwd')
        if not request.user.check_password(opw):
            error = "Original Password is Wrong"
            return render(request, 'compare/myaccount.html', {'id': nid, 'username': username, 'email': email, 'error': error})
        if npw != cpw:
            error = "Inconsistent new password entry"
            return render(request, 'compare/myaccount.html', {'id': nid, 'username': username, 'email': email, 'error': error})
        request.user.set_password(npw)
        request.user.save()
        logout(request)
        return render(request, 'compare/home.html')
    return render(request, 'compare/myaccount.html', {'id': nid, 'username': username, 'email': email})


def solutions(request):
    # When having DB, get the userid for post all the information between webpage
    # This sql statement need to be rewrite
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123123', db='mydb', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select id, solution from solutions")
    solution_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return render(request, 'compare/solutions.html', {'solution_list': solution_list})


def problems(request):
    # When having DB, get the userid for post all the information between webpage
    # This sql statement need to be rewrite
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123123', db='mydb', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select id, solution from solutions")
    problem_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return render(request, 'compare/myproblem.html', {'problem_list': problem_list})


def favourite(request):
    # When having DB, get the userid for post all the information between webpage
    # This sql statement need to be rewrite
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123123', db='mydb', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select id, solution from solutions")
    favourite_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return render(request, 'compare/favourite.html', {'favourite_list': favourite_list})
