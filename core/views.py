from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import UserForm
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from django.http import HttpResponse

# View for dashboard (index.html)
@login_required
def dashboard(request):
    return render(request, 'index.html')

# View for user management (already provided)
@login_required
def user_management(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'user_management.html', context)

# View for creating a permit
@login_required
def create_permit(request):
    if request.method == 'POST':
        # Handle permit creation logic here
        # Example: form = PermitForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     messages.success(request, "Permit created successfully!")
        #     return redirect('dashboard')
        pass
    return render(request, 'create_permit.html')

# View for custom reports
@login_required
def custom_reports(request):
    # Add logic to fetch and display reports if needed
    return render(request, 'custom_reports.html')

# View for help and support
@login_required
def help_support(request):
    return render(request, 'help_support.html')

# View for settings
@login_required
def settings(request):
    if request.method == 'POST':
        # Handle user settings update logic
        # Example: Update user profile or preferences
        pass
    return render(request, 'settings.html')

# View for login (handled by Django's auth system)
def login_view(request):
    if request.method == 'POST':
        # Handle login logic here using Django's auth system
        # Example: authenticate and login the user
        pass
    return render(request, 'login.html')

@login_required
@permission_required('user_management_app.can_manage_users', raise_exception=True)
def user_management(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'user_management.html', context)


@login_required
@permission_required('user_management_app.can_manage_users', raise_exception=True)
def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User added successfully!')
            return redirect('user_management')
    else:
        form = UserForm()
    
    context = {'form': form}
    return render(request, 'add_user.html', context)

@login_required
@permission_required('user_management_app.can_manage_users', raise_exception=True)
def edit_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully!')
            return redirect('user_management')
    else:
        form = UserForm(instance=user)
    
    context = {'form': form, 'user': user}
    return render(request, 'edit_user.html', context)


@login_required
@permission_required('user_management_app.can_manage_users', raise_exception=True)
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully!')
        return redirect('user_management')
    
    context = {'user': user}
    return render(request, 'delete_user.html', context)


def dashboard(request):
    return render(request, 'index.html')

def create_permit(request):
    return render(request, 'create_permit.html')

def view_permits(request):
    return render(request, 'view_permits.html')

def amend_permit(request):
    return render(request, 'amend_permit.html')

def issue_permit(request):
    return render(request, 'issue_permit.html')

def cancel_permit(request):
    return render(request, 'cancel_permit.html')

def print_permit(request):
    return render(request, 'print_permit.html')

def custom_reports(request):
    return render(request, 'custom_reports.html')

def day_end_report(request):
    return render(request, 'day_end_report.html')

def monthly_reports(request):
    return render(request, 'monthly_reports.html')

def traffic_escort_report(request):
    return render(request, 'traffic_escort_report.html')

def fee_breakdown(request):
    return render(request, 'fee_breakdown.html')

def ad_hoc_reports(request):
    return render(request, 'ad_hoc_reports.html')

def user_management(request):
    return render(request, 'user_management.html')

def data_management(request):
    return render(request, 'data_management.html')

def settings(request):
    return render(request, 'settings.html')

def security(request):
    return render(request, 'security.html')

def help_support(request):
    return render(request, 'help_support.html')

def logout_view(request):
    # Add your logout logic here
    return render(request, 'login.html')

def payment(request):
    return render(request, 'payment.html')

def view_statement(request):
    # Handle the logic for retrieving account statements based on date range
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    # Dummy data for now, replace with actual query
    statements = [
        {'date': '2025-01-01', 'description': 'Loaded Funds', 'amount': 100.00},
        {'date': '2025-01-05', 'description': 'Permit Fee', 'amount': -50.00},
    ]
    context = {'statements': statements, 'start_date': start_date, 'end_date': end_date}
    return render(request, 'view_statement.html', context)

def process_payment(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        payment_method = request.POST.get('payment_method')
        # Render the success page with context
        return render(request, 'payment_success.html', {
            'amount': amount,
            'payment_method': payment_method
        })
    return redirect('payment')

def payment_success(request):
    return render(request, 'payment_success.html')