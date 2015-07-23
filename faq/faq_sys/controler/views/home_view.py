from django.shortcuts import render_to_response
from django.template import Context

def home(request):
    return render_to_response('home.html',Context({'is_sign_in': request.session.get('is_sign_in')}))
