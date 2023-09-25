# Create your custom_views here.
import datetime
import json
import logging
from typing import Any, Dict

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView




logger = logging.getLogger(__name__)
my_util = MyUtil()
email_util = EmailUtil()


class GenericDashboardView(LoginRequiredMixin):
    login_url = "login"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["site"] = settings.SITE
        context["dashboard"] = True
        return context
    

class DashboardView(GenericDashboardView, TemplateView):
    """
    Dashboard
    profile update
    """

    template_name = "dashboard.html"
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["site"] = settings.SITE
        context["site"]["title"] = f"{_('Dashboard')} - {context['site']['_title']}"
        user = self.request.user


