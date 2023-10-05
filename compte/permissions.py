from django.contrib.auth.mixins import LoginRequiredMixin # this mixin is used in class based views for login required
from django.contrib.auth.decorators import login_required # this decorator is used in function based views for login required

from functools import wraps # import wraps from functools to use in decorator

from django.contrib.auth.mixins import UserPassesTestMixin # this mixin is used in class based views for user passes test
from django.http import HttpResponseForbidden # import http response forbidden from django
from django.core.exceptions import PermissionDenied # import permission denied from django 

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


def role_required(required_roles: list):
    
    def decorator(view_func):
        
        @wraps(view_func)
        
        def _wrapped_view(request, *args, **kwargs):
            
            if request.user.is_authenticated and  any(getattr(request.user, role) for role in required_roles):
                return view_func(request, *args, **kwargs)
            
            else:
                raise PermissionDenied
            
        return _wrapped_view
        
    return decorator


def payment_stil_valid(user):
    plan = SubcribePlam.objects.filter(user=user, still_valid=True)
    return plan.get_still_valid()

def group_required(required_groups: list):
        
        def decorator(view_func):
            
            @wraps(view_func)
            
            def _wrapped_view(request, *args, **kwargs):
                
                if request.user.is_authenticated: 
                    if request.user.groups.filter(name__in=required_groups).exists():
                       
                        if payment_stil_valid(request.user):
                            
                            return view_func(request, *args, **kwargs)
                        else:
                            pass
                            # redirect to payment page 
                    else:
                        # redirect to payment page
                        pass
                else:
                    raise PermissionDenied
                
            return _wrapped_view
            
        return decorator


class RoleRequiredMixin(UserPassesTestMixin):
    role_required = []
    
    def test_func(self):
        return self.request.user.is_authenticated and any(getattr(self.request.user, role) for role in self.role_required)


class GroupRequiredMixin(UserPassesTestMixin):
    """ 
    Name: GroupRequiredMixin
    Description: This mixin is used in class based views for group required
    
    """
    group_required = [] # list of group required
    
    def test_func(self):
        """ 
        Name: test_func
        Description: This function is used to test if user is authenticated and if user is in group required
        """
        return self.request.user.is_authenticated and self.request.user.groups.filter(name__in=self.group_required).exists()    
    

# importation 



from .models import SubcribePlam, User

ct = ContentType.objects.get_for_model(User)

#permission = Permission.objects.create(codename='can_view_payment_history', name='Can view payment history', content_type=ct)






