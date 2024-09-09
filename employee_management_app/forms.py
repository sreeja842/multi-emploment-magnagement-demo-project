from django import forms
from .models import Employee, Department, Role

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user', 'company', 'department', 'name', 'email', 'phone_number', 'role', 'joining_date']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_name', 'company']

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['role_name']