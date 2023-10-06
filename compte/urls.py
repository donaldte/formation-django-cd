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
    path('reset-password-email/', views.RessetPassworLinkView.as_view(), name='reset-password-email'),
    path('reset-password/<uid64>/<token>/', views.password_reset_verification, name='reset-password-verify'),
    path('reset-password-complete/', views.password_reset_html, name='reset-password-complete'),
]


urlpatterns += custom_patterns