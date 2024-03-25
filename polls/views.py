from django.shortcuts import HttpResponse

def index(request):
    lastest_question_list = Question.onjects.order_by("-pub_date"[:5])
    output = ", ".join([q.question_text for q in lastest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You are looking at question %s." % question_id)

def results(request, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)
    
def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)




"""
Esta documentado porque es un simple hola mundo

def index(request):

    return HttpResponse("Hola mundo")
"""