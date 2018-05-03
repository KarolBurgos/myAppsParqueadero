from rest_framework import serializers
from .models import Cliente

class VehiculoSerializers(serializers.ModelSerializer):
	"""docstring for ClassName"""
	class Meta:
		"""docstring for Meta"""
		model = Cliente
		fields = '__all__'
			

