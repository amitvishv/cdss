from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from doctorapp.models import DoctorModel, HospitalModel, User, MedicalHistory


class UserAdmin(BaseUserAdmin):
    list_display = (
    'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'hospitalname')
    add_fieldsets = (
        ("Add Doctor", {
            'classes': ('wide',),
            'fields': (
            'first_name', "username", 'is_staff', 'is_active', 'last_name', 'password1', 'password2', 'hospitalname')}
         ),
    )


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'event_type', 'description', 'file')


class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ('adharno', 'file', 'timestamp')


admin.site.register(DoctorModel, DoctorAdmin)
admin.site.register(MedicalHistory, MedicalHistoryAdmin)
admin.site.register(HospitalModel)
admin.site.register(User, UserAdmin)
