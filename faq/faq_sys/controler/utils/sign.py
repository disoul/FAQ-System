__author__ = 'yuwei'
from faq.faq_sys.models import *

def verify_sign_in(request):
    if is_sign_in_correct(request):
        record_sign_status(request)
        print(request.session.get('is_sign_in'))
        return True
    else:
        return False


def is_sign_in_correct(request):
    print(request.POST['email'])
    try:
        user = User.objects.get(email=request.POST['email'])
        real_password = user.password
        input_password = request.POST['password']
        return real_password == input_password
    except User.DoesNotExist:
        return False

def save_user(request):
    user = User()
    user.name = request.POST['username']
    print(user.name)
    user.email = request.POST['email']
    user.password = request.POST['password']
    user.save()

def record_sign_status(request):
    request.session['is_sign_in'] = True  # session记录登录状态
    request.session['email'] = request.POST['email']


def is_legal_sign_up(request):
    all_users = User.objects.all()
    for user in all_users:
        if user.name == request.POST['username'] or user.email == request.POST['email']:
            return False
    return True
