from rest_framework import serializers
from doctorapp.models import Doctor, MedicalHistory


class DoctorSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['doctor_id'] = self.context.get('request').user.id
        obj = Doctor.objects.create(**validated_data)
        return obj

    class Meta():
        model = Doctor
        fields = (
            'event_type',
            'description',
            'file',
            'timestamp'
        )

class MedicalHistorySerializer(serializers.ModelSerializer):

    class Meta():
        model = MedicalHistory
        fields = '__all__'

