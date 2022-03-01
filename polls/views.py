from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list= Question.onjects.order_by()
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    return HttpResponse("you're looking at question %s" % question_id)


def results(request, question_id):
    return HttpResponse("you're looking at the results of question %s" % question_id)


def vote(request, question_id):
    return HttpResponse("you're voting on question %s" % question_id)
