from rest_framework.parsers import FormParser, MultiPartParser
from doctorapp.models import Doctor, MedicalHistory
from doctorapp.serializers import DoctorSerializer, MedicalHistorySerializer
from rest_framework import generics
from rest_framework import permissions
from doctorapp.helpers import IsDoctor


class DoctorApiView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,IsDoctor)
    parser_classes = (MultiPartParser, FormParser)
    model = Doctor
    serializer_class = DoctorSerializer


class HistoryListApiView(generics.ListAPIView):

    permission_classes = (
        permissions.IsAuthenticated, IsDoctor
    )
    model = MedicalHistory
    serializer_class = MedicalHistorySerializer

    def get_queryset(self):
        adharno = self.request.query_params.get('adharno')
        obj_queryset = MedicalHistory.objects.filter(id=adharno)
        return obj_queryset