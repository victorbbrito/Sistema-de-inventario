# Generated by Django 4.1 on 2023-04-11 19:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("nobreak", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="nobreak",
            name="numero_serie",
            field=models.CharField(
                default="VERIFICAR",
                help_text="Ex:BRJ4030HPS",
                max_length=100,
                verbose_name="Número de Série",
            ),
            preserve_default=False,
        ),
    ]
