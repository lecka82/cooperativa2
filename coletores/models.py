from django.db import models

class Coletor(models.Model):
    TIPO_DOC = [("CPF", "CPF"), ("RG", "RG"), ("CNH", "CNH")]

    nome = models.CharField(max_length=120)
    tipo_documento = models.CharField(max_length=10, choices=TIPO_DOC, default="CPF")
    documento = models.CharField(max_length=20, unique=True)
    faz_parte_cooperativa = models.BooleanField(default=False)

    email = models.EmailField(blank=True, null=True, verbose_name="E-mail")
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)

    foto = models.ImageField(upload_to="fotos_coletores/", blank=True, null=True)

    # Dados bancários (opcionais) para repasse
    banco = models.CharField(max_length=50, blank=True, null=True)
    agencia = models.CharField(max_length=10, blank=True, null=True)
    numero_conta = models.CharField(max_length=20, blank=True, null=True)
    TIPO_CONTA = [("corrente", "Conta Corrente"), ("poupanca", "Poupança")]
    tipo_conta = models.CharField(max_length=10, choices=TIPO_CONTA, blank=True, null=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Coletor"
        verbose_name_plural = "Coletores"
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} ({self.documento})"
