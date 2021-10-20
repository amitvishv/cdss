from django.db import models
from doctorapp.helpers import ChoiceMaxlength, EventChoice, UserType
from django.contrib.auth.models import AbstractUser


class Hospital(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.name


class User(AbstractUser):
    hospitalname = models.ForeignKey(
        Hospital,
        related_name='hospitalname',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    user_type = models.CharField(
        max_length=ChoiceMaxlength,
        choices=UserType,
        default='Admin',
        help_text="Please Select one of them"
    )
class MedicalHistory(models.Model):
    adharno = models.CharField(max_length=12, default="0")
    file = models.FileField(upload_to='medical-history')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.adharno)

class Doctor(models.Model):
    event_type = models.CharField(
        max_length=ChoiceMaxlength,
        choices=EventChoice,
        help_text="Please Select one of them"
    )
    description = models.TextField()
    file = models.FileField(upload_to='upload-by-doctor')
    doctor = models.ForeignKey(User, related_name='doctorname', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.doctor.username
