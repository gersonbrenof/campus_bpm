from django.db import models

class Musicas(models.Model):
    link = models.URLField()
    def __str__(self):
        return self.link

class Bpm(models.Model):
    historico = models.JSONField(default=list, blank=True)
    notificacao = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.historico