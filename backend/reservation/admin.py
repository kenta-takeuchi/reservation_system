from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Calendar
from .models import Clinic
from .models import Department
from .models import ReservationFrame
from .models import Reservation

admin.site.register(User, UserAdmin)
admin.site.register(Calendar)
admin.site.register(Clinic)
admin.site.register(Department)
admin.site.register(ReservationFrame)
admin.site.register(Reservation)