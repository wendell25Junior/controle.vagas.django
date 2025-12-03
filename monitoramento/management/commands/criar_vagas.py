from django.core.management.base import BaseCommand
from monitoramento.models import Vaga

class Command(BaseCommand):
    help = 'Cria uma vaga nova'

    def add_arguments(self, parser):
        parser.add_argument('numero')
        parser.add_argument('setor')

    def handle(self, *args, **kwargs):
        numero = kwargs['numero']
        setor = kwargs['setor']

        vaga = Vaga.objects.create(
            numero=numero,
            setor=setor
        )

        self.stdout.write(self.style.SUCCESS(f"Vaga criada: {vaga}"))
