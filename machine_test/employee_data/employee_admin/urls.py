from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_employee, name='add_employee'),
    path('view/', views.view_employees, name='view_employees'),
    path('remove/<int:id>/', views.remove_employee, name='remove'),
    path('promote/<int:emp_id>/', views.promote_employee, name='promote_employee'),
]
