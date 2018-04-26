from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db import models
from django.urls import reverse

class Cliente(models.Model):
	"""docstring for ClassName"""
	identificacion = models.CharField(max_length=50,primary_key=True)
	nombre = models.CharField(max_length=60)
	apellido = models.CharField(max_length=60)
	telefono = models.CharField(max_length=60)

	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse('cliente-list')

class Vehiculo(models.Model):
	"""docstring for ClassName"""
	placa= models.CharField(max_length=50)
	marca = models.CharField(max_length=50)
	color = models.CharField(max_length=50)
	foto = models.ImageField(upload_to='photos/')
	idcliente = models.ForeignKey('Cliente',on_delete=models.PROTECT)
	
	def __str__(self):
		return self.placa

	def get_absolute_url(self):
		return reverse('vehiculo-list')
# Create your models here.

@receiver(post_delete,sender=Vehiculo)
def photo_delete(sender,instance,**kwargs):
	"""Borra los ficheros de las fotos que se eliminan"""
	instance.foto.delete(False)
