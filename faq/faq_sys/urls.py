from django.conf.urls import include,url
from .controler.views.home_view import *


urlpatterns = [url(r'^$', home)
]


