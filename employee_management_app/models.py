from django.db import models
from django.contrib.auth.models import User

# Company model
class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)

    def __str__(self):
        return self.name

# Role model
class Role(models.Model):
    role_name = models.CharField(max_length=50)

    def __str__(self):
        return self.role_name

# Department model
class Department(models.Model):
    department_name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.department_name

# Employee model
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    joining_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    clock_in = models.DateTimeField()
    clock_out = models.DateTimeField(null=True, blank=True)
    date = models.DateField()

class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee.name} - Leave from {self.start_date} to {self.end_date}"