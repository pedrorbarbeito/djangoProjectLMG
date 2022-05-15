from django.db import models

# Create your models here.
class Agenda(models.Model):
   ID = models.AutoField(primary_key=True)
   nombre = models.CharField(max_length=100)
   apellido = models.CharField(max_length=100)
   telefono = models.CharField(max_length=9)

   def __str__(self):
       return f"{self.nombre}, {self.apellido}, {self.telefono}"