from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages
from compte.permissions import role_required, RoleRequiredMixin, GroupRequiredMixin, group_required
from compte.models import Plan, SubcribePlam

class DashboardView(GroupRequiredMixin, View):
    group_required = ['basic', 'premium', 'New']
    template_name = 'dash/dashboard.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class AnalysComplexDataView(GroupRequiredMixin, View):
    group_required = ['premium']
    template_name = 'dash/analys_complex_data.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
    

class AnalysSimpleDataView(GroupRequiredMixin, View):
    group_required = ['New']
    template_name = 'dash/analys_simple_data.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
    
    
@group_required(['basic'])
def student_dashboard(request):
    
    user = request.user 
    
    if user.has_perm('compte.can_view_payment_history'): #app_label.codename
        
        messages.info(request, 'you can view payment history ')
    else:
        messages.info(request, 'you can not view payment history')   
        
    if user.groups.filter(name='basic').exists():
        messages.info(request, 'you are in basic group')     

    return render(request, 'dash/student_dashboard.html')


from django.contrib.auth.models import Group, Permission
import datetime 


def payment(request, *args, **kwargs):
    plans = Plan.objects.all()
    
    if request.method == 'POST':
        user = request.user 
        plan_id = request.POST.get('type_plan')
        
        period = request.POST.get('period')
        if plan_id == 'premium':
            if period=='monthly':
                SubcribePlam.objects.create(user=user, plan_id=plan_id,
                                            start_date=datetime.datetime.now(),
                                            end_date=datetime.datetime.now() + datetime.timedelta(days=30))
            elif period == 'yearly':
                
                SubcribePlam.objects.create(user=user, plan_id=plan_id,
                                            start_date=datetime.datetime.now(),
                                            end_date=datetime.datetime.now() + datetime.timedelta(days=365))
                    
            permission = Permission.objects.get(codename='can_view_payment_history')
            
            user.user_permissions.add(permission)
            
            messages.info(request, 'you have  been added to view history payment')
            
            groups = Group.objects.filter(name__in=['premium', 'basic', 'New'])
        
        
            user.groups.set(groups)
            
            messages.info(request, 'you have  been added to basic group')
            
            messages.success(request, 'you have successfully subscribed to a plan')
            
        elif plan_id == 'basic':
            SubcribePlam.objects.create(user=user, plan_id=plan_id,
                                        start_date='2023-10-05',
                                        end_date='2023-12-01')
            
            groups = Group.objects.filter(name__in=['basic', 'New'])
        
        
            user.groups.set(groups)
            
            messages.info(request, 'you have  been added to basic group')
            
            messages.success(request, 'you have successfully subscribed to a plan')   
        else:
            SubcribePlam.objects.create(user=user, plan_id=plan_id,
                                        start_date='2023-10-05',
                                        end_date='2023-12-01')
            
            groups = Group.objects.filter(name__in=['New'])
        
        
            user.groups.set(groups)
            
            messages.info(request, 'you have  been added to New group')
            
            messages.success(request, 'you have successfully subscribed to a plan')     
    return render(request, 'dash/payment.html', {'plans': plans})


