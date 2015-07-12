from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404


from faq.faq_sys.controler.utils.page import response_home_page, return_to_home
from faq.faq_sys.controler.utils.sign import verify_sign_in, save_user, record_sign_status, is_legal_sign_up


def home(request):
    homepage = get_template('home.html')
    return HttpResponse(homepage.render())


def sign_up(request):
    return render_to_response("sign_up.html")

def sign_up_form(request):
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    elif not is_legal_sign_up(request):
        return HttpResponse('注册信息有误，已存在的用户名或者邮箱' + return_to_home)
    else:
        save_user(request)
        record_sign_status(request)
        return response_home_page(request)


def sign_in(request):
    return render_to_response("sign_in.html")

def sign_in_form(request):
    if request.method == 'POST':
        if verify_sign_in(request):
            return response_home_page(request)
        else:
            return HttpResponse('登录信息错误' + return_to_home)
    else:
        return render_to_response("verify_sign_in.html")


