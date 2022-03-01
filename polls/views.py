from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.http import Http404

def index(request):
    latest_question_list= Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context ={
        'latest_question_list': latest_question_list,
    }
    #output=",".join([q.question_text for q in latest_question_list])
    #return HttpResponse(template.render(context,request))
    return render(request, 'polls/index.html',context)


#giving myself a little 404 error if the user trys to request a question id that does not exist
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("whoopsie that doewsnt exist >_<")
    return render(request, 'polls/detail.html', {'question':question})
    #return HttpResponse("you're looking at question %s" % question_id)


def results(request, question_id):
    return HttpResponse("you're looking at the results of question %s" % question_id)


def vote(request, question_id):
    return HttpResponse("you're voting on question %s" % question_id)
