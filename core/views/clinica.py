from rest_framework.viewsets import ModelViewSet
from core.models import Clinica
from core.serializers import ClinicaSerializer


class ClinicaViewset(ModelViewSet):
    queryset = Clinica.objects.all()
    serializer_class = ClinicaSerializer
