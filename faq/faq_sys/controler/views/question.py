__author__ = 'yuwei'

from django.http import HttpResponseNotAllowed
from django.shortcuts import render_to_response
from django.template import Context

from ...model.save import save_answer
from ...model.models import Question, Answer

# 返回单个question页面
def question_page(request):
    if request.method == 'GET':
        question_id = request.GET['question_id']
        question = Question.objects.get(id=question_id)
        answers = Answer.objects.filter(question=question)
        return render_to_response('question.html', Context({'question': question, 'answers': answers}))
    else:
        return HttpResponseNotAllowed('GET')



def create_answer(request):
    if request.method == 'POST':
        save_answer(request)
    else:
        HttpResponseNotAllowed('POST')
