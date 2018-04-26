from django.shortcuts import render
from django.http import HttpResponse
from parqueadero.models import Cliente, Vehiculo
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView

# Create your views here.
def first_view(request):
	return HttpResponse('Esta es mi primera vista')
# Create your views here.
def cliente(request):
	cliente_list = Cliente.objects.all()
	context = {'object_list': cliente_list}
	return render(request, 'parqueadero/cliente.html',context)

def cliente_detail(request,cliente_id):
	cliente =Cliente.objects.get(identificacion=cliente_id)
	context = {'object':cliente}
	return render(request, 'parqueadero/cliente_detail.html',context)

class VehiculoListView(ListView):
	"""docstring for VehiculoListView"""
	model = Vehiculo

class VehiculoDetailView(DetailView):
	"""docstring for Vehiculo"""
	model = Vehiculo

def base(request):
	return render(request, 'base.html')

class VehiculoUpdate(UpdateView):
	"""docstring for ClassName"""
	model= Vehiculo
	fields = '__all__'

class VehiculoCreate(CreateView):
	"""docstring for Pho"""
	model = Vehiculo
	fields = '__all__'

class VehiculoDelete(DeleteView):
	"""docstring for VehiculoDelete"""
	model = Vehiculo
	success_url = reverse_lazy('vehiculo-list')