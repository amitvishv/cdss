from rest_framework.permissions import BasePermission

ChoiceMaxlength = 30

EventChoice = (
        ('Medical Test', 'Medical Test'),
        ('OPD', 'OPD'),
)

UserType = (
        ('Doctor', 'Doctor'),
        ('Admin', 'Admin'),
)

# Custom permission for users with "is_active" = True.
class IsDoctor(BasePermission):
    """
    Allows access only to "is_active" users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.user_type == 'Doctor'
