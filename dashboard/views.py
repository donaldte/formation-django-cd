from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from compte.permissions import role_required, RoleRequiredMixin


class DashboardView(RoleRequiredMixin, View):
    role_required = ['is_organization', 'is_student', 'is_professor']
    template_name = 'dash/dashboard.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


    
@role_required(['is_student', 'is_organization'])    
def student_dashboard(request):
    return render(request, 'dash/student_dashboard.html')