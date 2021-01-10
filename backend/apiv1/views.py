from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, permissions, generics, viewsets
from rest_framework.response import Response

from .serializers import (
    CalendarSerializer,
    ClinicSerializer,
    DepartmentSerializer,
    PatientSerializer,
    ReservationSerializer,
    ReservationFrameSerializer,
    StaffSerializer
)
from reservation.models import (
    Calendar,
    Clinic,
    Department,
    User,
    ReservationFrame,
    Reservation
)
from .permission import custome_permissions


class CalenderView(viewsets.ModelViewSet):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
    permission_classes = (custome_permissions.PatientOrStaffPermission,)


class ClinicView(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (custome_permissions.PatientOrStaffPermission,)


class PatientView(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff=False)
    serializer_class = PatientSerializer
    permission_classes = (custome_permissions.PatientOrStaffPermission, )


class StaffView(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = StaffSerializer
    permission_classes = (permissions.IsAuthenticated, )


class DoctorView(generics.ListAPIView):
    queryset = User.objects.filter(is_staff=False, user_type="3")
    serializer_class = StaffSerializer
    permission_classes = (custome_permissions.PatientOrStaffPermission,)
