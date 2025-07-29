from django.db import models

class Musicas(models.Model):
    link = models.URLField()
    def __str__(self):
        return self.link

class Registro(models.Model):
    data = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    def __str__(self):
        return self.data