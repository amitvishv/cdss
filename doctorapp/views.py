from rest_framework.parsers import FormParser, MultiPartParser
from doctorapp.models import DoctorModel, MedicalHistory
from doctorapp.serializers import FileSerializer, MedicalHistorySerializer
from rest_framework import generics
from rest_framework import permissions


class DoctorApiView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser)
    model = DoctorModel
    serializer_class = FileSerializer


class HistoryListApiView(generics.ListAPIView):

    permission_classes = (
        permissions.IsAuthenticated,
    )
    model = MedicalHistory
    serializer_class = MedicalHistorySerializer

    def get_queryset(self):
        adharno = self.request.query_params.get('adharno')
        obj_queryset = MedicalHistory.objects.filter(id=adharno)
        return obj_queryset