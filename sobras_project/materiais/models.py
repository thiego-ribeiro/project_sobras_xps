from django.db import models

# =========================
# CHOICES
# =========================

STATUS_CHOICES = (
    ('Disponível', 'Disponível'),
    ('Doado', 'Doado'),
)

UNIDADES_CHOICES = (
    ('g', 'Grama(s)'),
    ('kg', 'Quilo(s)'),
    ('mg', 'Miligrama(s)'),
    ('cm', 'Centímetro(s)'),
    ('m', 'Metro(s)'),
    ('mm', 'Milímetro(s)'),
    ('l', 'Litro(s)'),
    ('ml', 'Mililitro(s)'),
    ('un', 'Unidade(s)'),
)

# =========================
# SOBRA DE MATERIAL
# =========================

class SobraMaterial(models.Model):
    tipo = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    unidade = models.CharField(
        max_length=10,
        choices=UNIDADES_CHOICES,
        default='un'
    )
    data_registro = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Disponível'
    )

    def __str__(self):
        return f"{self.tipo} - {self.quantidade} {self.get_unidade_display()} ({self.status})"


# =========================
# IMAGENS DA SOBRA
# =========================

class ImagemDispositivo(models.Model):
    sobra = models.ForeignKey(
        SobraMaterial,
        related_name='imagens',
        on_delete=models.CASCADE
    )
    imagem = models.ImageField(upload_to='imagens_dispositivos/')

    def __str__(self):
        return f"Imagem de {self.sobra.tipo}"


# =========================
# SOLICITAÇÃO DE MATERIAIS
# =========================

class Solicitacao(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    justificativa = models.TextField()
    data_solicitacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome