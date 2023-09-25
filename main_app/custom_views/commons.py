from typing import Any, Dict

from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import resolve, reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'prep/index.html'
    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["site"] = settings.SITE
        return context
 

class AboutUsView(TemplateView):

    template_name = "prep/about.html"

    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["site"] = settings.SITE
        return context


class ContactUsView(TemplateView):

    template_name = "prep/contact.html"

    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["site"] = settings.SITE
        return context

  
class AboutUsView(TemplateView):
    template_name = "prep/about.html"

    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["site"] = settings.SITE
        return context

#class AboutView(View):
class AboutView(TemplateView):
    template_name = 'prep/about-us.html'
    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["site"] = settings.SITE
        return context
    

class TermOfUseView(TemplateView):

    template_name = "prep/contact.html"

    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["site"] = settings.SITE
        return context

class SupportView(TemplateView):

    template_name = "prep/support.html"

    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["site"] = settings.SITE
        return context


class ContactUsView(TemplateView):

    template_name = "prep/contact.html"

    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["site"] = settings.SITE
        return context

class PrivacyPolicyView(TemplateView):

    template_name = "prep/contact.html"

    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["site"] = settings.SITE
        return context
    
class ComplaintsView(TemplateView):

    template_name = "prep/contact.html"

    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["site"] = settings.SITE
        return context
    
class FeedbackView(TemplateView):

    template_name = "prep/contact.html"

    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["site"] = settings.SITE
        return context

class ServicesView(TemplateView):

    template_name = "prep/services.html"

    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["site"] = settings.SITE
        return context