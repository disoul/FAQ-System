__author__ = 'yuwei'
from .models import *


def save_user(request):
    user = User(name=request.POST['name'],
                email=request.POST['email'],
                password=request.POST['password'])

    print(user.name)
    user.save()

def save_question(request):
    question = Question(title=request.POST['title'],
                        content=request.POST['content'],
                        user=User.objects.get(email=request.POST['email']))
    print(question.title)
    question.save()

def save_answer(request):
    answer = Answer(user=User.objects.get(email=request.POST['email']),
                    qustion=Question.objects.get(id=request.POST['id']),
                    content=request.POST['content'])
    print(answer)
    answer.save()
