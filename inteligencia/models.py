from django.db import models
from django.template.defaultfilters import truncatechars


# Create your models here.
class PostGrad(models.Model):
    title = models.CharField(max_length=10, verbose_name="Posto/Graduação")

    class Meta:
        ordering = ["id"]
        verbose_name = "Post/Grad"
        verbose_name_plural = "Post/Grad"

    def __str__(self):
        return self.title
    

class Policial(models.Model):
    SUBUNIDADE_CHOICES = (
        ("EM", "Estado Maior"),
        ("1CIA", "1ª Cia"),
        ("2CIA", "2ª Cia"),
        ("3CIA", "3ª Cia"),
        ("4CIA", "4ª Cia"),
        ("OUTRA", "Outra"),
    )

    CONDUTA_CHOICES = (
        ("SN", "Sem Novidade"),
        ("CN", "Com Novidade"),
        ("PN", "Possível Novidade"),
    )

    conduta = models.CharField(max_length=2, choices=CONDUTA_CHOICES, blank=True, null=True, verbose_name="Conduta")
    post_grad = models.ForeignKey(PostGrad, on_delete=models.PROTECT, related_name="policiais", verbose_name="Post/Grad")
    re =models.CharField(max_length=9, unique=True, null=False, blank=False, verbose_name="R.E.")
    nome_guerra = models.CharField(max_length=50, verbose_name="Nome de Guerra",)
    nome_completo = models.CharField(max_length=100, verbose_name="Nome Completo")
    opm = models.CharField(max_length=50, null=True, blank=True, verbose_name="OPM")
    subunidade = models.CharField(max_length=5, choices=SUBUNIDADE_CHOICES, blank=True, null=True, verbose_name="Subunidade")
    situacao = models.CharField(max_length=50, blank=True, null=True, verbose_name="Situação")
    consulta = models.TextField(blank=True, null=True, verbose_name="Consulta")
    p2 = models.TextField(blank=True, null=True, verbose_name="P2")
    jd = models.TextField(blank=True, null=True, verbose_name="JD")
    observacao = models.TextField(blank=True, null=True, verbose_name="Observações")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    @property
    def Consulta(self):
        return truncatechars(self.consulta, 30)
    
    @property
    def P2(self):
        return truncatechars(self.p2, 30)
    
    @property
    def JD(self):
        return truncatechars(self.jd, 30)
    
    @property
    def Observação(self):
        return truncatechars(self.observacao, 30)

    class Meta():
        ordering = ["post_grad__id"]
        verbose_name = "Policial"
        verbose_name_plural = "Policiais"

    def __str__(self):
        return self.nome_guerra