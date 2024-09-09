from django.urls import path
from . import views


urlpatterns = [
    # Dashboard URLs
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('hr_manager_dashboard/', views.hr_manager_dashboard, name='hr_manager_dashboard'),
    path('manager_dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('employee_dashboard/', views.employee_dashboard, name='employee_dashboard'),

    # Employee URLs
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/create/', views.create_employee, name='create_employee'),
    path('employees/update/<int:pk>/', views.update_employee, name='update_employee'),
    path('employees/delete/<int:pk>/', views.delete_employee, name='delete_employee'),

    # Department URLs
    path('departments/', views.department_list, name='department_list'),
    path('departments/create/', views.create_department, name='create_department'),
    path('departments/update/<int:pk>/', views.update_department, name='update_department'),
    path('departments/delete/<int:pk>/', views.delete_department, name='delete_department'),

    # Role URLs
    path('roles/', views.role_list, name='role_list'),
    path('roles/create/', views.create_role, name='create_role'),
    path('roles/update/<int:pk>/', views.update_role, name='update_role'),
    path('roles/delete/<int:pk>/', views.delete_role, name='delete_role'),

    path('clock_in/', views.clock_in, name='clock_in'),
    path('clock_out/<int:attendance_id>/', views.clock_out, name='clock_out'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('submit_leave/', views.submit_leave, name='submit_leave'),
    path('leave/', views.leave_list, name='leave_list'),
]