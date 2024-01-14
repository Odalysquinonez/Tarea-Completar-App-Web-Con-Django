from django.db import models


# Create your models here.


class Auto(models.Model):
    Modelo = models.CharField(max_length=255)
    Marca = models.CharField(max_length=255)
    Color = models.CharField(max_length=255)
    Anio = models.IntegerField()

    def __str__(self):
        return f' Auto {self.Modelo}: {self.Marca} {self.Color} {self.Anio}'


from django.db import models

# Create your models here.
