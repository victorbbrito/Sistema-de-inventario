from django.db import models
from cpu.models import Cpu
from monitore.models import Monitor
from nobreak.models import Nobreak

# Lista de setores (NOME NO PAINEL DE ADM, NOME NO DB) 
LISTA_SETORES = (
    ("AP - AGENTES DE PORTARIA", "AP - AGENTES DE PORTARIA"),
    ("BSEC - BIBLIOTECA SECUNDÁRIA", "BSEC - BIBLIOTECA SECUNDÁRIA"),
    ("CGP - CENTRAL DE GESTÃO DE PROJETOS", "CGP - CENTRAL DE GESTÃO DE PROJETOS"),
    ("DMKT - DEPARTAMENTO DE MARKETING", "DMKT - DEPARTAMENTO DE MARKETING"),
    ("EQSUP - EQUIPE DE SUPORTE", "EQSUP - EQUIPE DE SUPORTE"),
    ("FIN - FINANÇAS", "FIN - FINANÇAS"),
    ("GRH - GESTÃO DE RECURSOS HUMANOS", "GRH - GESTÃO DE RECURSOS HUMANOS"),
    ("GSTR - GERENCIA DE SERVICO DE TRANSPORTE", "GSTR - GERENCIA DE SERVICO DE TRANSPORTE"),
    ("IPTI - INSTITUTO DE PESQUISA TECNOLÓGICA E INDUSTRIAL", "IPTI - INSTITUTO DE PESQUISA TECNOLÓGICA E INDUSTRIAL"),
    ("LCP - LABORATÓRIO DE CONTROLE DE PROCESSOS", "LCP - LABORATÓRIO DE CONTROLE DE PROCESSOS"),
    ("MCOM - COMUNICAÇÃO E MÍDIA", "MCOM - COMUNICAÇÃO E MÍDIA"),
    ("OP - OPERAÇÕES", "OP - OPERAÇÕES"),
    ("PLG - PLANEJAMENTO E GESTÃO", "PLG - PLANEJAMENTO E GESTÃO"),
    ("RH - RECURSOS HUMANOS", "RH - RECURSOS HUMANOS"),
    ("SDTI - SUPORTE E DESENVOLVIMENTO DE TECNOLOGIAS DA INFORMAÇÃO", "SDTI - SUPORTE E DESENVOLVIMENTO DE TECNOLOGIAS DA INFORMAÇÃO"),
    ("VND - VENDAS", "VND - VENDAS"),
    ("UNIDADE DE CONTROLE", "UNIDADE DE CONTROLE"),
)

class Controle(models.Model):
    nome = models.CharField(max_length=120,verbose_name="Nome")
    usuario_ad = models.CharField(max_length=50, verbose_name="Usuário AD")
    setor = models.CharField(max_length=120, verbose_name="Setor", choices=LISTA_SETORES)
    tombo_cpu = models.ForeignKey("cpu.Cpu", related_name="controle_cpu", on_delete=models.CASCADE)
    tombo_monitor_1 = models.ForeignKey("monitore.Monitor", related_name="controle_monitor_1", on_delete=models.CASCADE)
    tombo_monitor_2 = models.ForeignKey("monitore.Monitor", related_name="controle_monitor_2", on_delete=models.CASCADE,blank=True , null=True)
    tombo_nobreak = models.ForeignKey("nobreak.Nobreak", related_name="controle_nobreak", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

