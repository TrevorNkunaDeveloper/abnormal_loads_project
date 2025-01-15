from django.urls import path
from . import views  # Correct import statement for views

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Permit Management
    path('create-permit/', views.create_permit, name='create_permit'),
    path('view-permits/', views.view_permits, name='view_permits'),
    path('amend-permit/', views.amend_permit, name='amend_permit'),
    path('issue-permit/', views.issue_permit, name='issue_permit'),
    path('cancel-permit/', views.cancel_permit, name='cancel_permit'),
    path('print-permit/', views.print_permit, name='print_permit'),

    # Reports
    path('custom-reports/', views.custom_reports, name='custom_reports'),
    path('day-end-report/', views.day_end_report, name='day_end_report'),
    path('monthly-reports/', views.monthly_reports, name='monthly_reports'),
    path('traffic-escort-report/', views.traffic_escort_report, name='traffic_escort_report'),
    path('fee-breakdown/', views.fee_breakdown, name='fee_breakdown'),
    path('ad-hoc-reports/', views.ad_hoc_reports, name='ad_hoc_reports'),

    # User Management
    path('user-management/', views.user_management, name='user_management'),
    path('user-management/add/', views.add_user, name='add_user'),
    path('user-management/edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('user-management/delete/<int:user_id>/', views.delete_user, name='delete_user'),

    # Data Management
    path('data-management/', views.data_management, name='data_management'),

    # Settings
    path('settings/', views.settings, name='settings'),

    # Security
    path('security/', views.security, name='security'),

    # Payment Accounts
    path('payment/', views.payment, name='payment'),
    path('view-statement/', views.view_statement, name='view_statement'),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('payment-success/', views.payment_success, name='payment_success'),

    # Help & Support
    path('help-support/', views.help_support, name='help_support'),

    

    # Authentication
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
