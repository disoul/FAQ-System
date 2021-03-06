__author__ = 'yuwei'

from django.http import HttpResponse, HttpResponseNotAllowed

from .utils.page import response_home_page, return_to_home
from .utils.sign import *
from ..model.save import save_user, save_question


def ask(request):
    if request.method == 'POST' and is_sign_in(request):
        save_question(request)
    else:
        raise HttpResponseNotAllowed('POST')


def sign_up(request):
    if request.method != 'POST':
        HttpResponseNotAllowed('POST')
    elif not is_legal_sign_up(request):
        return HttpResponse('注册信息有误，已存在的用户名或者邮箱' + return_to_home)
    else:
        save_user(request)
        record_sign_status(request)
        return response_home_page(request)


def sign_in(request):
    if request.method == 'POST':
        if verify_sign_in(request):
            return response_home_page(request)
        else:
            return HttpResponse('登录信息错误' + return_to_home)
    else:
        HttpResponseNotAllowed('POST')


def sign_out(request):
    if request.method != 'POST':
        HttpResponseNotAllowed('POST')
    if request.session.get('is_sign_in'):
        delete_sign_in_session(request)
        return response_home_page()
    else:
        HttpResponseNotAllowed('POST')
