__author__ = 'yuwei'
from faq.faq_sys.model.models import *

def get_user(request):
    return User.objects.get(email=request.POST['email'])
