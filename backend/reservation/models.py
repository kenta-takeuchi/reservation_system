import uuid

from django.contrib.auth.models import PermissionsMixin, BaseUserManager, AbstractBaseUser
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        return user

    def create_user(self, email, password, **extra_fields):
        user = self._create_user(email, password, **extra_fields)
        user.user_type = "1"
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE = [
        ('1', '患者'),
        ('2', 'スタッフ'),
        ('3', '医師')
    ]

    email = models.EmailField(_('email'), max_length=255, unique=True)

    username = models.CharField(_('username'), max_length=100, blank=True)
    first_name = models.CharField(_('first name'), max_length=50, blank=True)
    last_name = models.CharField(_('last name'), max_length=50, blank=True)
    is_active = models.BooleanField(_('is active'), default=True)
    is_staff = models.BooleanField(_('is staff'), default=False)
    is_superuser = models.BooleanField(_('is superuser'), default=False)
    user_type = models.CharField(_('user type'), choices=USER_TYPE, max_length=1)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    department_name = models.CharField(max_length=10)

    def __str__(self):
        return self.department_name


class Clinic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    clinic_name = models.CharField(max_length=30)
    tel = models.CharField(max_length=11)
    zip_code = models.CharField(max_length=7)
    address = models.CharField(max_length=100)
    doctors = models.ManyToManyField(User, through="DoctorClinicRelation", related_name='clinics')
    departments = models.ManyToManyField(Department, related_name='clinics')

    def __str__(self):
        return self.clinic_name


class DoctorClinicRelation(models.Model):
    """医師とクリニックの中間テーブル"""
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class Calendar(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='calendar')
    date = models.DateField(null=False)
    business_start_time = models.TimeField(null=False)
    business_end_time = models.TimeField(null=False)

    def __str__(self):
        return f'{self.clinic} {self.date}'


class ReservationFrame(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='reservation_frames')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations_doctor', related_query_name='')
    start_date = models.DateTimeField()

    def __str__(self):
        return f'{self.clinic} {self.doctor} {self.start_date}'


class Reservation(models.Model):
    reservation_frame = models.OneToOneField(ReservationFrame, on_delete=models.CASCADE, related_name='reservation')
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservation_patient')
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f'{self.patient} ({self.reservation_frame})'
