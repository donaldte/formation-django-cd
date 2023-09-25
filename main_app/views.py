
from typing import Any, Dict
from django.conf import settings

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

from django.contrib.auth import login, authenticate
from django.utils.translation import gettext_lazy as _

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!")

 