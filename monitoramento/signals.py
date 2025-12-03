from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Sensor
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json

# Quando o sensor é atualizado, enviamos uma mensagem para o WebSocket
@receiver(post_save, sender=Sensor)
def enviar_atualizacao_sensor(sender, instance, **kwargs):
    channel_layer = get_channel_layer()

    dados = {
        "vaga": instance.vaga.numero,
        "ocupado": instance.ocupado,
    }

    # envia broadcast para todos conectados no grupo "vagas"
    async_to_sync(channel_layer.group_send)(
        "vagas",
        {
            "type": "atualizar_vaga",
            "message": dados
        }
    )
