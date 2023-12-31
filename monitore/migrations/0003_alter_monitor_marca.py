# Generated by Django 4.1.7 on 2023-03-21 19:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("monitore", "0002_alter_monitor_foto_equipamento"),
    ]

    operations = [
        migrations.AlterField(
            model_name="monitor",
            name="marca",
            field=models.CharField(
                choices=[
                    ("ACER", "ACER"),
                    ("AOC", "AOC"),
                    ("DELL", "DELL"),
                    ("HP", "HP"),
                    ("LENOVO", "LENOVO"),
                    ("LG", "LG"),
                    ("PCTOP", "PCTOP"),
                    ("POSITIVO", "POSITIVO"),
                    ("PROVIEW", "PROVIEW"),
                    ("SAMSUNG", "SAMSUNG"),
                    ("VXPRO", "VXPRO"),
                ],
                max_length=100,
            ),
        ),
    ]
