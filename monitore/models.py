from django.db import models
from django.utils import timezone

# Create your models here.

LISTA_MARCAS=(
    ('ACER','ACER'),
    ('AOC','AOC'),
    ('DELL','DELL'),
    ('HP','HP'),
    ('LENOVO','LENOVO'),
    ('LG','LG'),
    ('PCTOP','PCTOP'),
    ('POSITIVO','POSITIVO'),
    ('PROVIEW','PROVIEW'),
    ('SAMSUNG','SAMSUNG'),
    ('VXPRO','VXPRO'),
)

class Monitor(models.Model):
    tombo = models.IntegerField(primary_key=True, help_text="Ex: 6541", verbose_name="Tombo")
    numero_serie = models.CharField(max_length=100, help_text="Ex:BRJ4030HPS", verbose_name="Número de Série")
    marca = models.CharField(max_length=100,choices=LISTA_MARCAS)
    foto_equipamento = models.ImageField(upload_to='photos_cpu',help_text="Faça aqui o upload das fotos do equipamento.",blank=True ,verbose_name="Foto do Equipamento")
    data_edicao = models.DateTimeField(default=timezone.now, verbose_name="Data de Edição")

    def __str__(self):
        return "{}".format(self.tombo)



