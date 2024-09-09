from rest_framework import viewsets
from .models import Employee, Department, Role, Company
from .serializers import EmployeeSerializer, DepartmentSerializer, RoleSerializer, CompanySerializer
from .models import Attendance, LeaveRequest
from .serializers import AttendanceSerializer, LeaveRequestSerializer
from rest_framework.permissions import IsAuthenticated

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Limit employee access to the company of the logged-in user
        company = self.request.user.employee.company
        return Employee.objects.filter(company=company)

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        company = self.request.user.employee.company
        return Department.objects.filter(company=company)

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        company = self.request.user.employee.company
        return Attendance.objects.filter(employee__company=company)

class LeaveRequestViewSet(viewsets.ModelViewSet):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        company = self.request.user.employee.company
        return LeaveRequest.objects.filter(employee__company=company)