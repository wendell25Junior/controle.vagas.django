from django.shortcuts import render
from django.http import JsonResponse
from .models import Andar, Setor, Vaga, Sensor
import json
from django.shortcuts import render
from .models import Vaga


def listar_andar(request):
    dados = [
        {
            "id": a.id,
            "numero": a.numero,
            "descricao": a.descricao
        } for a in Andar.objects.all()
    ]
    return JsonResponse(dados, safe=False)


def listar_setores(request):
    dados = [
        {
            "id": s.id,
            "nome": s.nome,
            "andar": s.andar.numero
        } for s in Setor.objects.all()
    ]
    return JsonResponse(dados, safe=False)


def listar_vagas(request):
    dados = [
        {
            "id": v.id,
            "codigo": v.codigo,
            "setor": v.setor.nome,
            "status": v.status
        } for v in Vaga.objects.all()
    ]
    return JsonResponse(dados, safe=False)


def evento_sensor(request, sensor_id):
    if request.method == "POST":
        body = json.loads(request.body)
        ocupado = body.get("ocupado")

        sensor = Sensor.objects.get(id=sensor_id)
        vaga = sensor.vaga

        vaga.status = ocupado
        vaga.save()

        evento = EventoVaga.objects.create(vaga=vaga, ocupado=ocupado)

        return JsonResponse({
            "mensagem": "Evento registrado",
            "vaga": vaga.codigo,
            "ocupado": ocupado,
            "evento_id": evento.id
        })

    return JsonResponse({"erro": "Método não permitido"}, status=405)


def home(request):
    return render(request, "home.html")

def dashboard(request):
    return render(request, "dashboard.html")

def G1(request):
    return render(request, "G1.html")


def dashboard(request):
    setores = {
        "A": Vaga.objects.filter(setor="A").order_by("numero"),
        "B": Vaga.objects.filter(setor="B").order_by("numero"),
        "C": Vaga.objects.filter(setor="C").order_by("numero"),
    }
    return render(request, "dashboard.html", {"setores": setores})