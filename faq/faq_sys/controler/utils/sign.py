__author__ = 'yuwei'
from faq.faq_sys.model.models import *
from faq.faq_sys.model.get import get_user

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
        user = get_user()
        real_password = user.password
        input_password = request.POST['password']
        return real_password == input_password
    except User.DoesNotExist:
        return False


def record_sign_status(request):
    request.session['is_sign_in'] = True  # session记录登录状态
    request.session['email'] = request.POST['email']


def is_legal_sign_up(request):
    all_users = User.objects.all()
    for user in all_users:
        if user.name == request.POST['username'] or user.email == request.POST['email']:
            return False
    return True

def is_sign_in(request):
    return request.session.get('is_sign_in')


# 将session里关于sign_in的内容置空
def delete_sign_in_session(request):
    request.session['is_sign_in'] = False
    request.session['email'] = None
