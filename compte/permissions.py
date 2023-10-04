from django.contrib.auth.mixins import LoginRequiredMixin # this mixin is used in class based views for login required
from django.contrib.auth.decorators import login_required # this decorator is used in function based views for login required

from functools import wraps # import wraps from functools to use in decorator

from django.contrib.auth.mixins import UserPassesTestMixin # this mixin is used in class based views for user passes test
from django.http import HttpResponseForbidden # import http response forbidden from django
from django.core.exceptions import PermissionDenied # import permission denied from django 




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


class RoleRequiredMixin(UserPassesTestMixin):
    role_required = []
    
    def test_func(self):
        return self.request.user.is_authenticated and any(getattr(self.request.user, role) for role in self.role_required)
    
    




