from django.db import models

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

class SobraMaterial(models.Model):
    tipo = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    unidade = models.CharField(max_length=10, choices=UNIDADES_CHOICES, default='un')
    data_registro = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Disponível')

    def __str__(self):
        return f"{self.tipo} - {self.quantidade} {self.get_unidade_display()} ({self.status})"
