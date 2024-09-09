from rest_framework.routers import DefaultRouter
from .views_api import EmployeeViewSet, DepartmentViewSet, RoleViewSet, CompanyViewSet
from .views_api import AttendanceViewSet, LeaveRequestViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'leave_requests', LeaveRequestViewSet)

urlpatterns = router.urls