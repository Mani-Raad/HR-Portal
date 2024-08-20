"""office_emp_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from .views import edit_employee
from .views import employee_detail
from .views import hr_employees , landing_page, hr_login, employee_login
from .views import  remove_emp, internal_message
from django.conf.urls.static import static
from .views import logout_view

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('login/', views.login, name='login'),
    path('hr_login/', views.hr_login, name='hr_login'),
    path('employee_login/', views.employee_login, name='employee_login'),
    path('index', views.index, name='index'),
     path('hr_home', views.hr_home, name='hr_home'),
     path('employee_home', views.employee_home, name='employee_home'),
    path('leave_manager/', views.leave_manager, name='leave_manager'),
    path('posh/', views.posh, name='posh'),
      path('sales_employees/', views.sales_employees, name='sales_employees'),
       path('hr_employees/', views.hr_employees, name='hr_employees'),
       path('it_employees/', views.it_employees, name='it_employees'),
       path('management/', views.management, name='manaegement'),
       path('finance_employees/', views.finance_employees, name='finance_employees'),
     path('digital_employees/', views.digital_employees, name='digital_employees'),
    path('all_emp', views.all_emp, name='all_emp'),
    path('add_emp', views.add_emp, name='add_emp'),
     path('employee_detail/<int:pk>/', employee_detail, name='employee_detail'),
    path('edit_employee/<int:emp_id>/', edit_employee, name='edit_employee'),
    path('remove_emp', views.remove_emp, name='remove_emp'),
    path('remove_emp/<int:emp_id>', views.remove_emp, name='remove_emp'),
    path('filter_emp', views.filter_emp, name='filter_emp'),
    path('<int:pk>/', views.hr_employees, name='hr_employees'),
    path('internal_message/', internal_message, name='internal_message'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('leave-manager/', views.leave_manager, name='leave_manager'),
    path('payroll/', views.payroll, name='payroll'),
    path('posh/', views.posh, name='posh'),
    path('leave-manager/', views.leave_manager, name='leave_manager'),
    path('leave-balance/', views.leave_balance, name='leave_balance'),
    path('apply-leave/', views.apply_leave, name='apply_leave'),
    path('leave-status/', views.leave_status, name='leave_status'),
    path('leave-history/', views.leave_history, name='leave_history'),
    path('leave-calendar/', views.leave_calendar, name='leave_calendar'),
    path('report-now/', views.report_now, name='report_now'),
    path('documents/', views.documents, name='documents'),
    path('reach_us/', views.reach_us, name='reach_us'),
     path('department/<int:department_id>/', views.department_employees, name='department_employees'),
    path('employee/<int:employee_id>/', views.employee_detail, name='employee_detail'),
     path('logout/', logout_view, name='logout'),
    path('hr_department/', views.hr_department, name='hr_department'),
   
    path('hr_payroll/', views.hr_payroll, name='hr_payroll'),
    path('hr_posh/', views.hr_posh, name='hr_posh'),
    path('hr_internal_message/', views.hr_internal_message, name='hr_internal_message'),
    path('hr_sales_employees/', views.hr_sales_employees, name='hr_sales_employees'),
       path('hr_hr_employees/', views.hr_hr_employees, name='hr_hr_employees'),
       path('hr_it_employees/', views.hr_it_employees, name='hr_it_employees'),
    path('hr_management/', views.hr_management, name='hr_management'),
       path('hr_finance_employees/', views.hr_finance_employees, name='hr_finance_employees'),
        path('payroll/', views.payroll, name='payroll'),
        path('employee_payroll/', views.employee_payroll, name='employee_payroll'),
        
    path('employee-request/', views.employee_request, name='employee_request'),
    path('view-generate/', views.view_generate, name='view_generate'),
    path('pay-slip/<str:employee_id>/', views.pay_slip, name='pay_slip'),
    path('hr_leave_manager/', views.hr_leave_manager, name='hr_leave_manager'),
    path('pending/', views.pending_requests, name='pending_requests'),
    path('history/', views.history, name='history'),
    path('calendar/', views.calendar, name='calendar'),
    path('swap/', views.swap, name='swap'),

   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
