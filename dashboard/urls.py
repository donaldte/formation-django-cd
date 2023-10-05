from django.urls import path 
from . import views 

app_name = 'dashboard'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('student/', views.student_dashboard, name='student-dashboard'),
    path('payment/', views.payment, name='payment')
]
