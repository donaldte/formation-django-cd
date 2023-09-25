# Create your custom_views here.
import json
import logging
from typing import Any, Dict

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.core.cache import cache
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView
from formtools.wizard.views import SessionWizardView


class SignupView(TemplateView):
    """Sign up page"""

    template_name = "account/signup.html"

    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["site"] = settings.SITE
        context["site"]["title"] = f"{_('Sign Up')} - {context['site']['_title']}"
        """
        context["form"] = RegistrationForm(
            initial={
                "is_superuser": False,
            }
        )"""
        return context

"""class RegisterView(SessionWizardView):"""
class RegisterView(TemplateView):
    
    """Sign up page + Organisation creation"""
    template_name = "account/register.html" 
"""
    form_list = [("account_data", RegistrationForm), ("org_data", OrganisationForm)]
    initial_dict = {
        "account_data": {
            "is_superuser": False,
        }
    }"""
    