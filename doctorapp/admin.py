from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from doctorapp.models import Doctor, Hospital, User, MedicalHistory


class UserAdmin(BaseUserAdmin):
    list_display = (
    'username', 'first_name', 'last_name', 'email', 'user_type', 'is_staff', 'is_active', 'date_joined', 'hospitalname')
    add_fieldsets = (
        ("Add Doctor", {
            'classes': ('wide',),
            'fields': (
            'first_name', "username", 'user_type', 'is_staff', 'is_active', 'last_name', 'password1', 'password2', 'hospitalname' )}
         ),
    )


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'event_type', 'description', 'file')


class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ('adharno', 'file', 'timestamp')


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(MedicalHistory, MedicalHistoryAdmin)
admin.site.register(Hospital)
admin.site.register(User, UserAdmin)
