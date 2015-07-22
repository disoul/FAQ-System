from django.contrib import admin
from .model.models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Question)
admin.site.register(Answer)
# admin.site.register(Comment)
