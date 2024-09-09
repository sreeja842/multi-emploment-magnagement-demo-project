from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Company, Employee, Department, Role, Attendance, LeaveRequest
from .forms import EmployeeForm, DepartmentForm, RoleForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required, permission_required

# Admins: Can manage all data within their own company
@permission_required('employee_management_app.view_company', raise_exception=True)
def admin_dashboard(request):
    # Get the admin's company based on their user
    company = get_object_or_404(Company, employee__user=request.user)
    
    # Filter employees and departments by the admin's company
    employees = Employee.objects.filter(company=company)
    departments = Department.objects.filter(company=company)
    
    return render(request, 'admin_dashboard.html', {'company': company, 'employees': employees, 'departments': departments})
# For HR Managers
@permission_required('employee_management_app.view_employee', raise_exception=True)
def hr_manager_dashboard(request):
    # Get the HR Manager's company based on their user
    company = get_object_or_404(Company, employee__user=request.user)
    
    # Filter employees and departments by the HR Manager's company
    employees = Employee.objects.filter(company=company)
    departments = Department.objects.filter(company=company)
    
    return render(request, 'hr_manager_dashboard.html', {'company': company, 'employees': employees, 'departments': departments})

# Managers: Can manage employees within their department
@permission_required('employee_management_app.view_department', raise_exception=True)
def manager_dashboard(request):
    department = get_object_or_404(Department, employee__user=request.user)
    employees = Employee.objects.filter(department=department)
    
    return render(request, 'manager_dashboard.html', {'department': department, 'employees': employees})

# Employees: Can view and update their own profile
@permission_required('employee_management_app.view_employee', raise_exception=True)
def employee_dashboard(request):
    employee = get_object_or_404(Employee, user=request.user)
    return render(request, 'employee_dashboard.html', {'employee': employee})

# -------------------- CRUD Operations for Employee ------------------------

@permission_required('employee_management_app.add_employee', raise_exception=True)
def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})

@permission_required('employee_management_app.view_employee', raise_exception=True)
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

@permission_required('employee_management_app.change_employee', raise_exception=True)
def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form})

@permission_required('employee_management_app.delete_employee', raise_exception=True)
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'confirm_delete.html', {'object': employee})

# -------------------- CRUD Operations for Department ----------------------

@permission_required('employee_management_app.add_department', raise_exception=True)
def create_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'department_form.html', {'form': form})

@permission_required('employee_management_app.view_department', raise_exception=True)
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

@permission_required('employee_management_app.change_department', raise_exception=True)
def update_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'department_form.html', {'form': form})

@permission_required('employee_management_app.delete_department', raise_exception=True)
def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return render(request, 'confirm_delete.html', {'object': department})

# -------------------- CRUD Operations for Role ----------------------------

@permission_required('employee_management_app.add_role', raise_exception=True)
def create_role(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('role_list')
    else:
        form = RoleForm()
    return render(request, 'role_form.html', {'form': form})

@permission_required('employee_management_app.view_role', raise_exception=True)
def role_list(request):
    roles = Role.objects.all()
    return render(request, 'role_list.html', {'roles': roles})

@permission_required('employee_management_app.change_role', raise_exception=True)
def update_role(request, pk):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('role_list')
    else:
        form = RoleForm(instance=role)
    return render(request, 'role_form.html', {'form': form})

@permission_required('employee_management_app.delete_role', raise_exception=True)
def delete_role(request, pk):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'POST':
        role.delete()
        return redirect('role_list')
    return render(request, 'confirm_delete.html', {'object': role})

# Clock-in an employee
@login_required
def clock_in(request):
    employee = Employee.objects.get(user=request.user)
    attendance = Attendance.objects.create(
        employee=employee,
        clock_in_time=timezone.now()
    )
    return redirect('attendance_list')

# Clock-out an employee
@login_required
def clock_out(request, attendance_id):
    attendance = Attendance.objects.get(id=attendance_id)
    attendance.clock_out_time = timezone.now()
    attendance.save()
    return redirect('attendance_list')

# View Attendance Records
@login_required
def attendance_list(request):
    employee = Employee.objects.get(user=request.user)
    attendance_records = Attendance.objects.filter(employee=employee)
    return render(request, 'attendance_list.html', {'attendance_records': attendance_records})

# Submit a leave request
@login_required
def submit_leave(request):
    employee = Employee.objects.get(user=request.user)
    if request.method == 'POST':
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        reason = request.POST['reason']
        LeaveRequest.objects.create(
            employee=employee,
            start_date=start_date,
            end_date=end_date,
            reason=reason
        )
        return redirect('leave_list')
    return render(request, 'submit_leave.html')

# View Leave Requests
@login_required
def leave_list(request):
    employee = Employee.objects.get(user=request.user)
    leave_requests = LeaveRequest.objects.filter(employee=employee)
    return render(request, 'leave_list.html', {'leave_requests': leave_requests})