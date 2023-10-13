from django.urls import path 
from . import views

from .custom_views import CreatePlanView, ListPlanView, CreatePlanView2

app_name = 'compte'

custom_patterns = [
    path('create-plan/', CreatePlanView.as_view(), name='create-plan'),
    path('create-plan2/', CreatePlanView2.as_view(), name='create-plan2'),
    path('list-plan/', ListPlanView.as_view(), name='list-plan'),
]


urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('activate/<uid64>/<token>/', views.activate, name="activate"),
    path('logout/', views.logout_view, name='logout'),
    path('reset-password-email/', views.ResetPassworLinkView.as_view(), name='reset-password-email'),
    path('reset-password/<uid64>/<token>/', views.password_reset_verification, name='reset-password-verify'),
    path('reset-password-complete/', views.password_reset_html, name='reset-password-complete'),
]


urlpatterns += custom_patterns


# Bon  a savoir django possede de vue preconstruite 

# exemple:

from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    # ... your other URL patterns ...

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]