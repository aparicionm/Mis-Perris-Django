from django.db import models
from django.utils import timezone

class Postulante(models.Model):
    correo = models.EmailField()
    run = models.CharField(max_length=11)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_Nacimiento= models.DateField(
            default=timezone.now)
    numero = models.IntegerField()
    region = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    vivienda = models.CharField(max_length=30)
    fecha_de_ahora = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.run
