# Generated by Django 4.0.5 on 2022-09-01 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0002_alter_controle_tombo_cpu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controle',
            name='setor',
            field=models.CharField(choices=[('AP-DT - APOIO DT', 'AP-DT - APOIO DT'), ('AGELI - ARQUIVO GELI', 'AGELI - ARQUIVO GELI'), ('ASCOM - ASSESSORIA DE COMUNICAÇÃO', 'ASCOM - ASSESSORIA DE COMUNICAÇÃO'), ('ASGAB - ASSESSORIA DO GABINETE', 'ASGAB - ASSESSORIA DO GABINETE'), ('CSI - COORDENAÇÃO DE SISTEMAS INFORMATIZADOS', 'CSI - COORDENAÇÃO DE SISTEMAS INFORMATIZADOS'), ('DEPOSITO GEPA', 'DEPOSITO GEPA'), ('DAF - DIRETORIA ADMINISTRATIVO E FINANCEIRO', 'DAF - DIRETORIA ADMINISTRATIVO E FINANCEIRO'), ('DJ - DIRETORIA JURIDICA', 'DJ - DIRETORIA JURIDICA'), ('DT - DIRETORIA TECNICA', 'DT - DIRETORIA TECNICA'), ('GAB - GABINETE', 'GAB - GABINETE'), ('GCAP - GERENCIA DE CONTROLE AGROPECUARIO', 'GCAP - GERENCIA DE CONTROLE AGROPECUARIO'), ('GEAA - GERENCIA DE APOIO ADMINISTRATIVO', 'GEAA - GERENCIA DE APOIO ADMINISTRATIVO'), ('GEAC - GERENCIA DE ALMOXARIFADO E COMPRAS', 'GEAC - GERENCIA DE ALMOXARIFADO E COMPRAS'), ('GEAI - GERENCIA DE ANALISE DE INFORMATICA', 'GEAI - GERENCIA DE ANALISE DE INFORMATICA'), ('GECC - GERENCIA DE CONTRATOS E CONVENIOS', 'GECC - GERENCIA DE CONTRATOS E CONVENIOS'), ('GECF - GERENCIA DE CONTROLE FLORESTAL', 'GECF - GERENCIA DE CONTROLE FLORESTAL'), ('GECP - GERENCIA DE CONTROLE DE PESCA', 'GECP - GERENCIA DE CONTROLE DE PESCA'), ('GEFA - GERENCIA DE FISCALIZACAO', 'GEFA - GERENCIA DE FISCALIZACAO'), ('GELI - GERENCIA DE LICENCIAMENTO INDUSTRIAL', 'GELI - GERENCIA DE LICENCIAMENTO INDUSTRIAL'), ('GEOF - GERENCIA DE ORCAMENTO E FINANCAS', 'GEOF - GERENCIA DE ORCAMENTO E FINANCAS'), ('GEPA - GERENCIA DE PATRIMONIO', 'GEPA - GERENCIA DE PATRIMONIO'), ('GEPC - GERENCIA DE PESSOAL E CADASTRO', 'GEPC - GERENCIA DE PESSOAL E CADASTRO'), ('GEPR - GERENCIA DE PROTOCOLO', 'GEPR - GERENCIA DE PROTOCOLO'), ('GERH - GERENCIA DE RECURSOS HIDRICOS', 'GERH - GERENCIA DE RECURSOS HIDRICOS'), ('GERM - GERENCIA DE RECURSOS MINERAIS', 'GERM - GERENCIA DE RECURSOS MINERAIS'), ('GFAU - GERENCIA DE FAUNA', 'GFAU - GERENCIA DE FAUNA'), ('GGEO - GERENCIA DE GEOPROCESSAMENTO', 'GGEO - GERENCIA DE GEOPROCESSAMENTO'), ('NEA - NUCLEO DE EDUCACAO AMBIENTAL', 'NEA - NUCLEO DE EDUCACAO AMBIENTAL'), ('OUVIDARIA', 'OUVIDARIA'), ('PAD - PROCURADORIA ADMINISTRATIVA', 'PAD - PROCURADORIA ADMINISTRATIVA'), ('PJU - PROCURADORIA', 'PJU - PROCURADORIA'), ('PMA - PROCURADORIA DO MEIO AMBIENTE', 'PMA - PROCURADORIA DO MEIO AMBIENTE'), ('SETR - SERVICO DE TRANSPORTE', 'SETR - SERVICO DE TRANSPORTE'), ('SINDICANCIA', 'SINDICANCIA'), ('UNIDADE DE CONTROLE', 'UNIDADE DE CONTROLE')], max_length=120, verbose_name='Setor'),
        ),
    ]
