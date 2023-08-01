# Generated by Django 4.0.5 on 2022-08-31 17:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cpu',
            fields=[
                ('tombo', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('numero_serie', models.CharField(max_length=100)),
                ('hostname', models.CharField(max_length=100)),
                ('sistema_operacional', models.CharField(choices=[('WINDOWS 7', 'WINDOWS 7'), ('WINDOWS 10', 'WINDOWS 10'), ('WINDOWS 11', 'WINDOWS 11')], max_length=100)),
                ('processador', models.CharField(choices=[('AMD A8 - 5500', 'AMD A8 - 5500'), ('AMD A8 - 5500B', 'AMD A8 - 5500B'), ('AMD ATHLON 2 - X2', 'AMD ATHLON 2 - X2'), ('AMD ATHLON 2 - X4', 'AMD ATHLON 2 - X4'), ('AMD FX4100', 'AMD FX4100'), ('AMD FX4300', 'AMD FX4300'), ('INTEL CORE 2 DUO', 'INTEL CORE 2 DUO'), ('INTEL CORE 2 QUAD', 'INTEL CORE 2 QUAD'), ('INTEL i3 - 330', 'INTEL i3 - 330'), ('INTEL i3 - 2310M', 'INTEL i3 - 2310M'), ('INTEL i3 - 3240', 'INTEL i3 - 3240'), ('INTEL i3 - 9100F', 'INTEL i3 - 9100F'), ('INTEL i3 - 10100', 'INTEL i3 - 10100'), ('INTEL i5 - 650', 'INTEL i5 - 650'), ('INTEL i5 - 760', 'INTEL i5 - 760'), ('INTEL i5 - 2410M', 'INTEL i5 - 2410M'), ('INTEL i5 - 4430S', 'INTEL i5 - 4430S'), ('INTEL i5 - 7500', 'INTEL i5 - 7500'), ('INTEL i5 - 9400F', 'INTEL i5 - 9400F'), ('INTEL i5 - 10400', 'INTEL i5 - 10400'), ('INTEL i5 - 1135G7', 'INTEL i5 - 1135G7'), ('INTEL i7 - 3770', 'INTEL i7 - 3770'), ('INTEL i7 - 6500U', 'INTEL i7 - 6500U'), ('INTEL i7 - 8700', 'INTEL i7 - 8700'), ('INTEL i7 - 8700T', 'INTEL i7 - 8700T'), ('INTEL i7 - 9700', 'INTEL i7 - 9700'), ('INTEL i7 - 9700F', 'INTEL i7 - 9700F'), ('INTEL i7 - 9700K', 'INTEL i7 - 9700K'), ('INTEL i7 - 9700KF', 'INTEL i7 - 9700KF'), ('INTEL i7 - 10700', 'INTEL i7 - 10700'), ('INTEL i7 - 10700F', 'INTEL i7 - 10700F'), ('INTEL i7 - 1165G7', 'INTEL i7 - 1165G7'), ('INTEL i7 - 11700', 'INTEL i7 - 11700'), ('INTEL i7 - 11700F', 'INTEL i7 - 11700F'), ('INTEL i7 - 11700K', 'INTEL i7 - 11700K'), ('INTEL i7 - 11700KF', 'INTEL i7 - 11700KF'), ('INTEL i7 - 11800H', 'INTEL i7 - 11800H'), ('INTEL i7 - 12700', 'INTEL i7 - 12700'), ('INTEL i7 - 12700F', 'INTEL i7 - 12700F'), ('INTEL i7 - 12700K', 'INTEL i7 - 12700K'), ('INTEL i7 - 12700KF', 'INTEL i7 - 12700KF'), ('INTEL PENTIUM - E5200', 'INTEL PENTIUM - E5200'), ('INTEL PENTIUM - G620', 'INTEL PENTIUM - G620'), ('INTEL PENTIUM - G630', 'INTEL PENTIUM - G630'), ('INTEL XEON E3 - 1230', 'INTEL XEON E3 - 1230'), ('INTEL XEON E5 - 1603', 'INTEL XEON E5 - 1603')], max_length=100)),
                ('memoria_ram', models.CharField(choices=[('DDR2 - 2GB', 'DDR2 - 2GB'), ('DDR2 - 3GB', 'DDR2 - 3GB'), ('DDR2 - 4GB', 'DDR2 - 4GB'), ('DDR3 - 2GB', 'DDR3 - 2GB'), ('DDR3 - 4GB', 'DDR3 - 4GB'), ('DDR3 - 6GB', 'DDR3 - 6GB'), ('DDR3 - 8GB', 'DDR3 - 8GB'), ('DDR3 - 16GB', 'DDR3 - 16GB'), ('DDR4 - 8GB', 'DDR4 - 8GB'), ('DDR4 - 16GB', 'DDR4 - 16GB')], max_length=100)),
                ('placa_de_video', models.CharField(choices=[('SEM VIDEO OFFBOARD', 'SEM VIDEO OFFBOARD'), ('INTEL IRIS XE', 'INTEL IRIS XE'), ('GEFORCE 7200GS', 'GEFORCE 7200GS'), ('GEFORCE 7300SE', 'GEFORCE 7300SE'), ('GEFORCE 8400GS', 'GEFORCE 8400GS'), ('GEFORCE GT210', 'GEFORCE GT210'), ('GEFORCE GT710', 'GEFORCE GT710'), ('GEFORCE GT730', 'GEFORCE GT730'), ('NVIDIA GTX1050Ti', 'NVIDIA GTX1050Ti'), ('NVIDIA GTX1660', 'NVIDIA GTX1660'), ('NVIDIA GTX1660SUPER', 'NVIDIA GTX1660SUPER'), ('NVIDIA GTX1660Ti', 'NVIDIA GTX1660Ti'), ('NVIDIA QUADRO 2000', 'NVIDIA QUADRO 2000'), ('NVIDIA QUADRO K620', 'NVIDIA QUADRO K620'), ('NVIDIA RTX3050', 'NVIDIA RTX3050'), ('NVIDIA RTX3060', 'NVIDIA RTX3060'), ('RADEON 3000', 'RADEON 3000'), ('RADEON HD5450', 'RADEON HD5450'), ('RADEON HD7560D', 'RADEON HD7560D')], max_length=100)),
                ('hd', models.CharField(choices=[('SEM HD', 'SEM HD'), ('120GB', '120GB'), ('160GB', '160GB'), ('250GB', '250GB'), ('320GB', '320GB'), ('500GB', '500GB'), ('1TB', '1TB')], max_length=100)),
                ('ssd', models.CharField(choices=[('SEM SSD', 'SEM SSD'), ('120GB', '120GB'), ('240GB', '240GB'), ('480GB', '480GB')], max_length=100)),
                ('leitor_cd', models.CharField(choices=[('SIM', 'SIM'), ('NÃO', 'NÃo')], max_length=5)),
                ('data_edicao', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]