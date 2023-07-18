from django.db import models

class Nota(models.Model):
    nota = models.CharField(max_length=100)
    def __str__(self):
        return self.nota
