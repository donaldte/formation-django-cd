
from typing import Any, Dict
from django.conf import settings

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
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


def modify_dataset(request,*args, **kwargs):
    pk = kwargs.get('pk')
    try:
        if pk != None:
            form = DataTestForm()
            data = DataTest.objects.get(pk=pk)
            #data = get_object_or_404(DataTest, pk=pk)
            form = DataTestForm(instance=data)
            if request.method == 'POST':
                form = DataTestForm(request.POST, instance=data)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Dataset saved successfully modified.")
                    return redirect('main_app:list-dataset')
                else:
                    messages.error(request, "There is an error with your data!")
                    return render(request, 'main_app/modify_dataset.html', {'form': form})
                return render(request, 'main_app/modify_dataset.html', {'form': form})
    except Exception as e:
        messages.error(request, "Dataset not found.")
        return render(request, 'main_app/modify_dataset.html', {'form': form})  
          
    return render(request, 'main_app/modify_dataset.html', {'form': form})



def delete_dataset(request, *args, **kwargs):
    pk = kwargs.get('pk')
    try: 
        if pk != None:
            data = DataTest.objects.get(pk=pk)
            data.is_deleted = True
            data.save()
            messages.success(request, "Dataset deleted successfully.")
            return redirect('main_app:list-dataset')
    except Exception as e:
        messages.error(request, "Dataset not found.")
        return redirect('main_app:list-dataset')
    



def list_dataset(request, *args, **kwargs):
    try:
        data = DataTest.objects.filter(is_deleted=False)
    except Exception as e:
        messages.error(request, "Dataset empty.")
        return render(request, 'main_app/list_dataset.html', {'data': data})  
          
    return render(request, 'main_app/list_dataset.html', {'data': data})


def list_data(request, cls, template_name, *args, **kwargs):
    data = cls.objects.all()
    return render(request, template_name, {'data': data})



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


       