from django.contrib import admin
from django.urls import path, include
from monitoramento import views
from monitoramento.consumers import VagaConsumer
from monitoramento.views import dashboard
from monitoramento.models import Registro, Setor

urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/andares/', views.listar_andar),
    path('api/setores/', views.listar_setores),
    path('api/setor/', views.listar_setores),
    path('api/vagas/', views.listar_vagas),
    path('api/sensor/<int:sensor_id>/', views.evento_sensor),
    path('home/', views.home),
    path('dashboard/', views.dashboard),
    path('G1/', views.G1),
    path('dashboard/', dashboard, name="dashboard"),
    path('monitoramento/', include("monitoramento.urls")),

]

websocket_urlpatterns = [
    path("ws/vagas/", VagaConsumer.as_asgi()),
]























"""
URL configuration for sensorproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
