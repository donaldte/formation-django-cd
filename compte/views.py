from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail, EmailMessage

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

from .token import TokenGenerator

from .utils import send_email_with_html

generateToken = TokenGenerator()

def signup_view(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('compte:signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('compte:signup')
            else:
                user = User.objects.create_user(email=email, username=username, first_name=first_name, last_name=last_name, password=password1)
                user.is_active = False
                user.save()
                
                # welcome email 
                subject = " Welcome "
                message = f"Hi,{first_name} {last_name}, welcome on DEA your account has been created successfully."
                from_email = settings.EMAIL_HOST_USER
                to_email = [user.email]
                send_mail(subject, message, from_email, to_email, fail_silently=False)
                
                # activation email 
                current_site = get_current_site(request)
                email_subject = " confirm your email on DEA"
                context =  {
                        'name': f"{first_name} {last_name}",
                        'domain': current_site.domain,
                        'uid':  urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': generateToken.make_token(user)
                    }
                template_name = 'emailconfirm.html'
                
                send_email_with_html(context, template_name, email_subject, from_email, to_email)
                
                messages.success(request, 'Account created successfully but not yet activated till you confirm your email address')
                
                return redirect('compte:login')
        else:
            messages.error(request, "the two password must match")    
            
    return render(request, 'signup.html')


class ResetPassworLinkView(View):
    
    template_name = 'reset.html'
    
    
    def get(self, request,  *ags, **kwargs):
        return render(request, self.template_name)
    
    
    def post(self, request,  *args, **kwargs):
        
        email = request.POST.get('email')
        
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            
            from_email = settings.EMAIL_HOST_USER
            to_email = [user.email]
            
            # reset email 
            current_site = get_current_site(request)
            email_subject = " reset your password on DEA"
            context =  {
                    'name': f"{user.first_name} {user.last_name}",
                    'domain': current_site.domain,
                    'uid':  urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': generateToken.make_token(user)
                }
            email_template_name = 'email_reset_password.html'
            
            send_email_with_html(context, email_template_name, email_subject, from_email, to_email)
            
            messages.success(request, "check your mail box to reset your password")
        
        return render(request, self.template_name)


def password_reset_verification(request, uid64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        my_user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        my_user = None 
    
    if my_user is not None and generateToken.check_token(my_user, token):
        request.session['user_id'] = my_user.id
        messages.success(request, "Your can reset your password now")    
        return redirect('compte:reset-password-complete')
        
    else:
        messages.error(request, "reset failed try again")  
        
    return redirect('compte:reset-password-email') 


def password_reset_html(request):
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 == password2:
            user_id = request.session.get('user_id')
            user = User.objects.get(pk=user_id)
            user.set_password(password1)
            user.save()
            
            # Clear the session data after successful password reset
            del request.session['user_id']

            messages.success(request, "Your password has been reset successfully") 
            return redirect('compte:login')   
        else:
            messages.error(request, "the two password must match")

    return render(request, 'reset_password_form.html')

def login_view(request):
    next = request.GET.get('next')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        __user = User.objects.filter(username=username)
        if __user:
            if __user.first().is_active:
                if user is not None:
                    if user.is_active:
                        
                        login(request, user)
                        
                        messages.success(request, 'welcome back login has been done successfully')
                        
                        if next:
                            return redirect(next)
                        else:
                            return redirect('dashboard:dashboard')
                                   
                    else:
                        messages.info(request, 'Sorry you didn\'t confirm your account')    
                
                else:
                    messages.error(request, 'sorry your username and password didn\'t match')
                    return redirect('compte:login') 
            else:
                messages.info(request, 'Sorry you didn\'t confirm your account')        
    return render(request, 'login.html')



def activate(request, uid64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        my_user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        my_user = None 
    
    if my_user is not None and generateToken.check_token(my_user, token):
        my_user.is_active = True 
        my_user.save()  
        messages.success(request, "Your account has been activated you can login now")    
    else:
        messages.error(request, "Activation failed try again")  
        
    return redirect('compte:login')        



def logout_view(request):
    logout(request)
    messages.success(request, 'Your logged out')
    return redirect('compte:login')

