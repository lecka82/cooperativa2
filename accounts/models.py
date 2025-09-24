from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    CARGOS = [
        ("admin", "Administrador"),
        ("gestor", "Gestor"),
        ("operacional", "Operacional"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    foto = models.ImageField(upload_to="profiles/", blank=True, null=True)
    cargo = models.CharField(max_length=20, choices=CARGOS, default="operacional")

    def __str__(self):
        return f"Perfil de {self.user.username}"
