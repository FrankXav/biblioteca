from django.db import models

# Create your models here.

class Estante(models.Model):
    estante = models.CharField(max_length=100,blank=False, null=False)
    def __str__(self):
        return self.estante

class Repisa(models.Model):
    repisa = models.CharField(max_length=100,blank=False, null=False)
    def __str__(self):
        return self.repisa

class Libros(models.Model):
    nombre = models.CharField(max_length=500, blank=False, null=False)
    autor = models.CharField(max_length=500, blank=False, null=False)
    descripcion = models.CharField(max_length=500, blank=True)
    estante = models.ForeignKey(Estante,on_delete=models.CASCADE,blank=False, null=False)
    repisa = models.ForeignKey(Repisa,on_delete=models.CASCADE,blank=False, null=False)

    def __str__(self):
        return self.nombre

