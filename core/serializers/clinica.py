from rest_framework import ModelSerializer
from core.models import Clinica


class ClinicaSerializer(ModelSerializer):
    class Meta:
        model = Clinica
        field = '__all__'
