from rest_framework import serializers
from doctorapp.models import DoctorModel, MedicalHistory


class FileSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['doctor_id'] = self.context.get('request').user.id

        obj = DoctorModel.objects.create(**validated_data)
        return obj

    class Meta():
        model = DoctorModel
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

