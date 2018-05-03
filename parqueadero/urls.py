"""parqueaderoAppsfinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import  url
from parqueadero import views

urlpatterns = [
    url(r'^$',views.base,name='base'),
	path('',views.first_view, name='first-view'),
	url(r'^cliente/$', views.cliente, name='cliente-list'),
    url(r'^cliente/(?P<cliente_id>\d+)/detail/$', views.cliente_detail,	name='cliente-detail'),
    
	#url(r'^vehiculo/$', views.VehiculoListView.as_view(),name='vehiculo-list'),
    path('vehiculo/', views.VehiculoListView.as_view(), name='vehiculo-list'),
    # Detail
    path('vehiculo/<int:pk>/detail/', views.VehiculoDetailView.as_view(), name='vehiculo-detail'),
    # Update
    path('vehiculo/<int:pk>/update/', views.VehiculoUpdate.as_view(), name='vehiculo-update'),
    #Create
    path('vehiculo/create/', views.VehiculoCreate.as_view(), name='vehiculo-create'),
    #Delete
    path('vehiculo/<int:pk>/delete/', views.VehiculoDelete.as_view(), name='vehiculo-delete'),
    path('clien',views.VehiculoList.as_view(),name='vehiculo_listrest'),
    #url(r'^vehiculo/(?P<pk>\d+)/detail/$',views.VehiculoDetailView.as_view(),name='vehiculo-detail'),
    #url(r'^vehiculo/(?P<pk>\d+)/update/$', views.VehiculoUpdate.as_view(),name='vehiculo-update'),
    #url(r'^vehiculo/create/$', views.VehiculoCreate.as_view(), name='vehiculo-create'), 
    #url(r'^vehiculo/(?P<pk>\d+)/delete/$', views.VehiculoDelete.as_view(),name='vehiculo-delete'),

]
