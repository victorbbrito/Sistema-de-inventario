# Generated by Django 4.0.5 on 2022-09-01 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitore', '0002_alter_monitor_foto_equipamento'),
        ('controle', '0008_alter_controle_tombo_cpu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controle',
            name='tombo_monitor_2',
            field=models.ForeignKey(default='null', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='controle_monitor_2', to='monitore.monitor'),
        ),
    ]
