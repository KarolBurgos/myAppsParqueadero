from rest_framework import serializers
from Vehiculo.models import Vehiculo


class VehiculoSerializers(serializers.ModelSerializers):
	"""docstring for ClassName"""
	class Meta:
		model = Vehiculo
		fields = '__all__'
