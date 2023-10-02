from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.contrib.auth import authenticate, login


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
                
                """
                send and email to the user to confirm his account creation
                """
                messages.success(request, 'Account created successfully but not yet activated till you confirm your email address')
                
                return redirect('compte:login')
        else:
            messages.error(request, "the two password must match")    
            
    return render(request, 'signup.html')




def login_view(request):
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
                        
                    else:
                        messages.info(request, 'Sorry you didn\'t confirm your account')    
                
                else:
                    messages.error(request, 'sorry your username and password didn\'t match')
                    return redirect('compte:login') 
            else:
                messages.info(request, 'Sorry you didn\'t confirm your account')        
    return render(request, 'login.html')



