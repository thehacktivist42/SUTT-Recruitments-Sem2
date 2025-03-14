from django.http import HttpResponse
from .models import Question
from django.shortcuts import render, get_object_or_404

def index(request):
    latestQuestionList = Question.objects.order_by("-pubDate")[:5]
    output = ", ".join([q.questionText for q in latestQuestionList])
    context = {
        "latestQuestionList" : latestQuestionList,
    }
    return render(request, "polls/index.html", context)

def detail(request, questionID):
    return render(request, "polls/detail.html", {"question" : get_object_or_404(Question, pk = questionID)})

def results(request, questionID):
    return HttpResponse("You're looking at the results of the response %s." % questionID)

def vote(request, questionID):
    return HttpResponse("You're voting on question %s." % questionID)