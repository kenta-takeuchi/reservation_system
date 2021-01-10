from rest_framework import serializers

from backend.reservation.models import User
from backend.reservation.models import Calendar
from backend.reservation.models import Clinic
from backend.reservation.models import Department
from backend.reservation.models import ReservationFrame
from backend.reservation.models import Reservation


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", 'first_name', 'last_name', "password"]
        extra_kwargs = {"password": {"write_only": True, "required": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", 'first_name', 'last_name', "password", "user_type"]
        extra_kwargs = {"password": {"write_only": True, "required": True}}

    def create(self, validated_data):
        user = User.objects.create_superuser(**validated_data)
        return user


class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = ['clinic.id', 'doctor.id', 'date', 'business_start_time', 'business_end_time']


class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ['clinic_name', 'tel', 'zip_code', 'address', 'doctors', 'departments']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['department_name']


class ReservationFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationFrame
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

