from django.contrib import admin
from .models import Andar, Setor, Vaga, Sensor

# funções que o adm pode fazer
admin.site.register(Andar)
admin.site.register(Setor)
admin.site.register(Vaga)
admin.site.register(Sensor)



