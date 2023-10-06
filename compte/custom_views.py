from django import forms
from django.shortcuts import redirect, render
from django.urls import reverse 
from .models import Plan, SubcribePlam
from .custom_forms import PlanForm, PlanForm2
from django.views.generic import CreateView, ListView
from django.views import View

from django.contrib import messages


class ListPlanView(ListView):
        
    template_name = 'plan/list.html'
    
    model = Plan
    
    context_object_name = 'plans'
    
    def get_queryset(self):
        return Plan.objects.all()
        

class CreatePlanView(CreateView):
    
    form_class = PlanForm
    
    template_name = 'plan/create.html'
    
    model = Plan
    
    def get_success_url(self):
        messages.success(self.request, 'Plan created successfully')
        return reverse('compte:list-plan')



class CreatePlanView2(View):
    
    form_class = PlanForm2
    
    template_name = 'plan/create.html'
    
    def get_success_url(self):
        messages.success(self.request, 'Plan created successfully')
        return reverse('compte:list-plan')
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})
    
    def post(self, request, *args, **kwargs):
       
        form = self.form_class(request.POST)
        if form.is_valid():
            
            Plan.objects.create(
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                description=form.cleaned_data['description']
            )
            messages.success(self.request, 'Plan created successfully')
            return redirect('compte:list-plan')
        else:
            form = self.form_class(request.POST)
            return render(request, self.template_name, {'form': form})
    
        return render(request, self.template_name, {'form': self.form_class})
