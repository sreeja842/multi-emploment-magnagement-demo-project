from django.contrib import admin
from .models import Company, Employee, Role, Department

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'contact_info']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['user', 'company', 'role', 'joining_date']

admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)

# Register your models here.
