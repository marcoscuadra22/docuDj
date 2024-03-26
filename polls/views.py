from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import HttpResponse, render, get_object_or_404
from django.template import loader
from django.db.models import F
from django.urls import reverse

from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    return HttpResponse("You are looking at question %s." % question_id)

def results(request, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)
    
def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render (
            request,
            "polls/detail.html",
            {
              "question": question,
              "error_message": "You didn't select a choice",  
            },
        )
    else:
        selected_choice.votes = f("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reserve("polls:results", args=(question.id,)))
    
