import pymysql
from django.shortcuts import render
from .models import Problem, Dataset
from .forms import SubmitProbSpecForm


def home(request):
    context = {
        'posts': Problem.objects.all()
    }
    return render(request, 'compare/home.html', context)

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
    # When having DB, get the userid for post all the information between webpage
    # nid=request.GET.get('nid')
    # current_account_info = sqlhelper.get_one("select id, Username from user where id=%s",[nid],)
    return render(request, 'compare/myaccount.html')


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
    return render(request, 'compare/problems.html', {'problem_list': problem_list})


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
