
from typing import Any, Dict
from django.conf import settings

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

from django.contrib.auth import login, authenticate

from django.utils.translation import gettext_lazy as _

from django.contrib import messages

from main_app.models import DataTest

from .forms import DataTesFormWithoutModel, DataTestForm



def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!")
    


# def create_datesete(request, *args, **kwargs):
    
#     # create through forms 
#     form = DataTestForm(request.POST or None)
   
#     if request.method == 'POST':
#         form = DataTestForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = DataTestForm()
#             messages.success(request, "Dataset saved successfully.")
#             messages.success(request, "Dataset saved successfully.")
            
#     context = {
#         'form': form,
#     }        
    
#     return render(request, 'main_app/create_datesete.html', context) 


def create_datesete(request, *args, **kwargs):
    
   
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        if name == 'test':
            messages.error(request, "this is an invalid name for the file")
            return render(request, 'main_app/create_datasete1.html')
        data = DataTest.objects.create(name=name, description=description)
        if data:
            messages.success(request, "Dataset saved successfully.")
            messages.success(request, "Dataset saved successfully.")
             
    
    return render(request, 'main_app/create_datasete1.html') 

class DataSetCreationView(View):
    
    template_name = 'main_app/create_datesete.html'
    form = DataTesFormWithoutModel()
    context = {
        'form': form
    }
    
    def get(self, request, *args, **kwargs) -> int:
        return render(request, self.template_name, self.context)
    
    def post(self, request, *args, **kwargs):
        form = DataTesFormWithoutModel(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            data = DataTest.objects.create(name=name, description=description)
            if data:
                form = DataTesFormWithoutModel() 
                messages.success(request, _("Dataset saved successfully."))
                messages.success(request, _("Dataset saved successfully."))
        self.context['form'] = form    
        return render(request, self.template_name, self.context)


       