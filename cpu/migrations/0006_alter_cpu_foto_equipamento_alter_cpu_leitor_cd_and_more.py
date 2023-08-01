# Generated by Django 4.1.7 on 2023-03-21 19:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cpu", "0005_cpu_placa_de_video"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cpu",
            name="foto_equipamento",
            field=models.ImageField(
                blank=True,
                help_text="Faça aqui o upload das fotos do equipamento.",
                upload_to="photos_cpu",
                verbose_name="Foto do Equipamento",
            ),
        ),
        migrations.AlterField(
            model_name="cpu",
            name="leitor_cd",
            field=models.CharField(
                choices=[("SIM", "SIM"), ("NÃO", "NÃO"), ("EXTERNO", "EXTERNO")],
                max_length=10,
                verbose_name="Leitor de CD",
            ),
        ),
        migrations.AlterField(
            model_name="cpu",
            name="placa_de_video",
            field=models.CharField(
                choices=[
                    ("SEM VIDEO OFFBOARD", "SEM VIDEO OFFBOARD"),
                    ("INTEL IRIS XE", "INTEL IRIS XE"),
                    ("GEFORCE 7200GS", "GEFORCE 7200GS"),
                    ("GEFORCE 7300SE", "GEFORCE 7300SE"),
                    ("GEFORCE 8400GS", "GEFORCE 8400GS"),
                    ("GEFORCE GT210", "GEFORCE GT210"),
                    ("GEFORCE GT220", "GEFORCE GT220"),
                    ("GEFORCE GT710", "GEFORCE GT710"),
                    ("GEFORCE GT730", "GEFORCE GT730"),
                    ("NVIDIA GTX1050Ti", "NVIDIA GTX1050Ti"),
                    ("NVIDIA GTX1660", "NVIDIA GTX1660"),
                    ("NVIDIA GTX1660SUPER", "NVIDIA GTX1660SUPER"),
                    ("NVIDIA GTX1660Ti", "NVIDIA GTX1660Ti"),
                    ("NVIDIA QUADRO 2000", "NVIDIA QUADRO 2000"),
                    ("NVIDIA QUADRO K620", "NVIDIA QUADRO K620"),
                    ("NVIDIA RTX3050", "NVIDIA RTX3050"),
                    ("NVIDIA RTX3060", "NVIDIA RTX3060"),
                    ("RADEON 3000", "RADEON 3000"),
                    ("RADEON HD5450", "RADEON HD5450"),
                    ("RADEON HD7560D", "RADEON HD7560D"),
                ],
                max_length=100,
                verbose_name="Placa de Vídeo",
            ),
        ),
        migrations.AlterField(
            model_name="cpu",
            name="processador",
            field=models.CharField(
                choices=[
                    ("AMD A8 - 5500", "AMD A8 - 5500"),
                    ("AMD A8 - 5500B", "AMD A8 - 5500B"),
                    ("AMD ATHLON 2 - X2", "AMD ATHLON 2 - X2"),
                    ("AMD ATHLON 2 - X4", "AMD ATHLON 2 - X4"),
                    ("AMD FX4100", "AMD FX4100"),
                    ("AMD FX4300", "AMD FX4300"),
                    ("INTEL CORE 2 DUO", "INTEL CORE 2 DUO"),
                    ("INTEL CORE 2 QUAD", "INTEL CORE 2 QUAD"),
                    ("INTEL i3 - 330", "INTEL i3 - 330"),
                    ("INTEL i3 - 2310M", "INTEL i3 - 2310M"),
                    ("INTEL i3 - 3240", "INTEL i3 - 3240"),
                    ("INTEL i3 - 9100F", "INTEL i3 - 9100F"),
                    ("INTEL i3 - 10100", "INTEL i3 - 10100"),
                    ("INTEL i3 - 10105F", "INTEL i3 - 10105F"),
                    ("INTEL i5 - 650", "INTEL i5 - 650"),
                    ("INTEL i5 - 760", "INTEL i5 - 760"),
                    ("INTEL i5 - 2410M", "INTEL i5 - 2410M"),
                    ("INTEL i5 - 4430S", "INTEL i5 - 4430S"),
                    ("INTEL i5 - 7500", "INTEL i5 - 7500"),
                    ("INTEL i5 - 9400F", "INTEL i5 - 9400F"),
                    ("INTEL i5 - 10400", "INTEL i5 - 10400"),
                    ("INTEL i5 - 1135G7", "INTEL i5 - 1135G7"),
                    ("INTEL i7 - 3770", "INTEL i7 - 3770"),
                    ("INTEL i7 - 6500U", "INTEL i7 - 6500U"),
                    ("INTEL i7 - 8700", "INTEL i7 - 8700"),
                    ("INTEL i7 - 8700T", "INTEL i7 - 8700T"),
                    ("INTEL i7 - 9700", "INTEL i7 - 9700"),
                    ("INTEL i7 - 9700F", "INTEL i7 - 9700F"),
                    ("INTEL i7 - 9700K", "INTEL i7 - 9700K"),
                    ("INTEL i7 - 9700KF", "INTEL i7 - 9700KF"),
                    ("INTEL i7 - 10700", "INTEL i7 - 10700"),
                    ("INTEL i7 - 10700F", "INTEL i7 - 10700F"),
                    ("INTEL i7 - 1165G7", "INTEL i7 - 1165G7"),
                    ("INTEL i7 - 11700", "INTEL i7 - 11700"),
                    ("INTEL i7 - 11700F", "INTEL i7 - 11700F"),
                    ("INTEL i7 - 11700K", "INTEL i7 - 11700K"),
                    ("INTEL i7 - 11700KF", "INTEL i7 - 11700KF"),
                    ("INTEL i7 - 11800H", "INTEL i7 - 11800H"),
                    ("INTEL i7 - 12700", "INTEL i7 - 12700"),
                    ("INTEL i7 - 12700F", "INTEL i7 - 12700F"),
                    ("INTEL i7 - 12700K", "INTEL i7 - 12700K"),
                    ("INTEL i7 - 12700KF", "INTEL i7 - 12700KF"),
                    ("INTEL PENTIUM - E5200", "INTEL PENTIUM - E5200"),
                    ("INTEL PENTIUM - G620", "INTEL PENTIUM - G620"),
                    ("INTEL PENTIUM - G630", "INTEL PENTIUM - G630"),
                    ("INTEL XEON E3 - 1230", "INTEL XEON E3 - 1230"),
                    ("INTEL XEON E5 - 1603", "INTEL XEON E5 - 1603"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="cpu",
            name="ssd",
            field=models.CharField(
                choices=[
                    ("SEM SSD", "SEM SSD"),
                    ("120GB", "120GB"),
                    ("240GB", "240GB"),
                    ("256GB", "256GB"),
                    ("480GB", "480GB"),
                    ("512GB", "512GB"),
                ],
                max_length=100,
                verbose_name="SSD",
            ),
        ),
    ]
