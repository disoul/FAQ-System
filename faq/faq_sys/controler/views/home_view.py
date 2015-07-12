from django.http import HttpResponse
from django.template.loader import get_template


def home(request):
    homepage = get_template('home.html')
    return HttpResponse(homepage.render())
