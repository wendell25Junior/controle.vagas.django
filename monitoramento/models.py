from django.db import models

# Representa um andar do estacionamento
class Andar(models.Model):
    nome = models.CharField(max_length=10, unique=True)  # Ex: A, B, C…

    def __str__(self):
        return self.nome  # <---- Antes retornava 'None' causando erro no admin


# Setores dentro de um andar
class Setor(models.Model):
    nome = models.CharField(max_length=20)
    andar = models.ForeignKey(Andar, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - Andar {self.andar.nome}"


# Vagas dentro de um setor
class Vaga(models.Model):
    numero = models.IntegerField(unique=True)
    setor = models.CharField(max_length=1, choices=[("A","A"),("B","B"),("C","C")])
    ocupada = models.BooleanField(default=False)
    def __str__(self):
        return f"Vaga {self.numero} ({self.setor})"


# Sensores ligados às vagas
class Sensor(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    vaga = models.OneToOneField(Vaga, on_delete=models.CASCADE)

    def __str__(self):
        return f"Sensor {self.codigo} - {self.vaga}"


# Registros de leitura do sensor
class Registro(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    status = models.BooleanField()  # True = ocupado / False = livre
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sensor} - {'Ocupado' if self.status else 'Livre'}"
