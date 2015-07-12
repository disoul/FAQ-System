__author__ = 'yuwei'

from django.shortcuts import render_to_response
from django.template import Context
from django.shortcuts import render


return_to_home = "<a href='home'>点击回到首页</a>"

def response_home_page(request):
    return render_to_response('home.html', Context({'is_sign_in': request.session.get('is_sign_in')}))
