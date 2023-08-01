from django.db import models
from django.utils import timezone


# Create your models here.
LISTA_PROCESSADORES = (
    ('AMD A8 - 5500','AMD A8 - 5500'),
    ('AMD A8 - 5500B','AMD A8 - 5500B'),
    ('AMD ATHLON 2 - X2','AMD ATHLON 2 - X2'),
    ('AMD ATHLON 2 - X4','AMD ATHLON 2 - X4'),
    ('AMD FX4100','AMD FX4100'),
    ('AMD FX4300','AMD FX4300'),
    ('INTEL CORE 2 DUO','INTEL CORE 2 DUO'),
    ('INTEL CORE 2 QUAD','INTEL CORE 2 QUAD'),
    ('INTEL i3 - 330','INTEL i3 - 330'),
    ('INTEL i3 - 2310M','INTEL i3 - 2310M'),
    ('INTEL i3 - 3240','INTEL i3 - 3240'),
    ('INTEL i3 - 9100F','INTEL i3 - 9100F'),
    ('INTEL i3 - 10100','INTEL i3 - 10100'),
    ('INTEL i3 - 10105F','INTEL i3 - 10105F'),
    ('INTEL i5 - 650','INTEL i5 - 650'),
    ('INTEL i5 - 760','INTEL i5 - 760'),
    ('INTEL i5 - 2410M','INTEL i5 - 2410M'),
    ('INTEL i5 - 4430S','INTEL i5 - 4430S'),
    ('INTEL i5 - 7500','INTEL i5 - 7500'),
    ('INTEL i5 - 9400F','INTEL i5 - 9400F'),
    ('INTEL i5 - 10400','INTEL i5 - 10400'),
    ('INTEL i5 - 1135G7','INTEL i5 - 1135G7'),
    ('INTEL i7 - 3770','INTEL i7 - 3770'),
    ('INTEL i7 - 6500U','INTEL i7 - 6500U'),
    ('INTEL i7 - 8700','INTEL i7 - 8700'),
    ('INTEL i7 - 8700T','INTEL i7 - 8700T'),
    ('INTEL i7 - 9700','INTEL i7 - 9700'),
    ('INTEL i7 - 9700F','INTEL i7 - 9700F'),
    ('INTEL i7 - 9700K','INTEL i7 - 9700K'),
    ('INTEL i7 - 9700KF','INTEL i7 - 9700KF'),
    ('INTEL i7 - 10700','INTEL i7 - 10700'),
    ('INTEL i7 - 10700F','INTEL i7 - 10700F'),
    ('INTEL i7 - 1165G7','INTEL i7 - 1165G7'),
    ('INTEL i7 - 11700','INTEL i7 - 11700'),
    ('INTEL i7 - 11700F','INTEL i7 - 11700F'),
    ('INTEL i7 - 11700K','INTEL i7 - 11700K'),
    ('INTEL i7 - 11700KF','INTEL i7 - 11700KF'),
    ('INTEL i7 - 11800H','INTEL i7 - 11800H'),
    ('INTEL i7 - 12700','INTEL i7 - 12700'),
    ('INTEL i7 - 12700F','INTEL i7 - 12700F'),
    ('INTEL i7 - 12700K','INTEL i7 - 12700K'),
    ('INTEL i7 - 12700KF','INTEL i7 - 12700KF'),
    ('INTEL PENTIUM - E5200','INTEL PENTIUM - E5200'),
    ('INTEL PENTIUM - G620','INTEL PENTIUM - G620'),
    ('INTEL PENTIUM - G630','INTEL PENTIUM - G630'),
    ('INTEL XEON E3 - 1230','INTEL XEON E3 - 1230'),
    ('INTEL XEON E5 - 1603','INTEL XEON E5 - 1603'),
)

LISTA_MEMORIAS = (
    ('DDR2 - 2GB','DDR2 - 2GB'),
    ('DDR2 - 3GB','DDR2 - 3GB'),
    ('DDR2 - 4GB','DDR2 - 4GB'),
    ('DDR3 - 2GB','DDR3 - 2GB'),
    ('DDR3 - 4GB','DDR3 - 4GB'),
    ('DDR3 - 6GB','DDR3 - 6GB'),
    ('DDR3 - 8GB','DDR3 - 8GB'),
    ('DDR3 - 16GB','DDR3 - 16GB'),
    ('DDR4 - 8GB','DDR4 - 8GB'),
    ('DDR4 - 16GB','DDR4 - 16GB'),
)

LISTA_HDS = (
    ('SEM HD','SEM HD'),
    ('120GB','120GB'),
    ('160GB','160GB'),
    ('250GB','250GB'),
    ('320GB','320GB'),
    ('500GB','500GB'),
    ('1TB','1TB'),
)

LISTA_SSDS = (
    ('SEM SSD','SEM SSD'),
    ('120GB','120GB'),
    ('240GB','240GB'),
    ('256GB','256GB'),
    ('480GB','480GB'),
    ('512GB','512GB'),
)

LISTA_PLACAS_VIDEO = (
    ('SEM VIDEO OFFBOARD','SEM VIDEO OFFBOARD'),
    ('INTEL IRIS XE','INTEL IRIS XE'),
    ('GEFORCE 7200GS','GEFORCE 7200GS'),
    ('GEFORCE 7300SE','GEFORCE 7300SE'),
    ('GEFORCE 8400GS','GEFORCE 8400GS'),
    ('GEFORCE GT210','GEFORCE GT210'),
    ('GEFORCE GT220','GEFORCE GT220'),
    ('GEFORCE GT710','GEFORCE GT710'),
    ('GEFORCE GT730','GEFORCE GT730'),
    ('NVIDIA GTX1050Ti','NVIDIA GTX1050Ti'),
    ('NVIDIA GTX1660','NVIDIA GTX1660'),
    ('NVIDIA GTX1660SUPER','NVIDIA GTX1660SUPER'),
    ('NVIDIA GTX1660Ti','NVIDIA GTX1660Ti'),
    ('NVIDIA QUADRO 2000','NVIDIA QUADRO 2000'),
    ('NVIDIA QUADRO K620','NVIDIA QUADRO K620'),
    ('NVIDIA RTX3050','NVIDIA RTX3050'),
    ('NVIDIA RTX3060','NVIDIA RTX3060'),
    ('RADEON 3000','RADEON 3000'),
    ('RADEON HD5450','RADEON HD5450'),
    ('RADEON HD7560D','RADEON HD7560D'),
)

LISTA_SISTEMA = (
    ('WINDOWS 7','WINDOWS 7'),
    ('WINDOWS 10', 'WINDOWS 10'),
    ('WINDOWS 11', 'WINDOWS 11'),
)

LISTA_BOOLEAN = (
    ('SIM','SIM'),
    ('NÃO','NÃO'),
    ('EXTERNO','EXTERNO'),
)
# falta placa de video no adm
# opção externo pro leitor de cds

class Cpu(models.Model):
    tombo = models.IntegerField(primary_key=True,help_text="Ex: 6541", verbose_name="Tombo")
    numero_serie = models.CharField(max_length=100,help_text="Ex:BRJ4030HPS", verbose_name="Número de Série")
    hostname = models.CharField(max_length=100,help_text="Ex: WS-HP-GEAI-6541")
    sistema_operacional = models.CharField(max_length=100, choices=LISTA_SISTEMA, verbose_name="Sistema Operacional")
    processador = models.CharField(max_length=100, choices=LISTA_PROCESSADORES)
    memoria_ram = models.CharField(max_length=100, choices=LISTA_MEMORIAS, verbose_name="Memória Ram")
    placa_de_video = models.CharField(max_length=100, choices=LISTA_PLACAS_VIDEO, verbose_name="Placa de Vídeo")
    hd = models.CharField(max_length=100, choices=LISTA_HDS, verbose_name="HD")
    ssd = models.CharField(max_length=100, choices=LISTA_SSDS, verbose_name="SSD")
    leitor_cd = models.CharField(max_length=10, choices=LISTA_BOOLEAN, verbose_name="Leitor de CD")
    ip = models.CharField(max_length=20,help_text="Ex: 10.10.0.3",verbose_name="Endereço IP")
    mac = models.CharField(max_length=20,help_text="Ex: ", verbose_name="Endereço MAC")
    foto_equipamento = models.ImageField(upload_to='photos_cpu',help_text="Faça aqui o upload das fotos do equipamento.", verbose_name="Foto do Equipamento", blank=True)
    data_edicao = models.DateTimeField(default=timezone.now,verbose_name="Data de Edição")

    def __str__(self):
        return "{}".format(self.tombo)