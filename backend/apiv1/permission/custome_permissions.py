from rest_framework import permissions


class PatientOrStaffPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.user.is_staff:
            return True
        return obj.user.id == request.user.id


class StaffPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.user.is_staff is not True:
            return False
        if request.mothod in permissions.SAFE_METHODS:
            return True
        if obj.user.is_superuser:
            return True
        return obj.user.id == request.user.id

