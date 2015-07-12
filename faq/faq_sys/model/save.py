__author__ = 'yuwei'
from faq.faq_sys.model.models import *
from faq.faq_sys.model.get import get_user

def save_user(request):
    user = User(name=request.POST['name'],
                email=request.POST['email'],
                password=request.POST['password'])

    print(user.name)
    user.save()

def save_question(request):
    question = Question(content=request.POST['content'],
                        date=request.POST['date'],
                        content=request.POST['content'],
                        user=get_user(request))
    print(question.title)
    question.save()
