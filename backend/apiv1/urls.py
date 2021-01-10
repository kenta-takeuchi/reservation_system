from django.urls import path, include
from rest_framework import routers

from .views import (
    CalenderView,
    ClinicView,
    DoctorView,
    DepartmentView,
    StaffView,
    PatientView
)

router = routers.DefaultRouter()
router.register('calendar', CalenderView)
router.register('clinic', ClinicView)
router.register('department', DepartmentView)
router.register('staff', StaffView, 'staff')
router.register('patient', PatientView)

app_name = 'apiv1'

urlpatterns = [
    path('', include(router.urls)),
    path('doctor/', DoctorView.as_view(), name='doctor_list')
]
