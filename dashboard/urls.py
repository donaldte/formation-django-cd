from django.urls import path 
from . import views 

app_name = 'dashboard'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('student/', views.student_dashboard, name='student-dashboard'),
    path('payment/', views.payment, name='payment'),
    path('task/', views.my_task_view, name='task'),
    path('task_result/<str:task_id>/', views.my_task_result, name='task-result'),
]
