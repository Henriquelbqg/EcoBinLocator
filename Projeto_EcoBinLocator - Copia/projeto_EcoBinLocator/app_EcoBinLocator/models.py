from django.db import models

def upload_image(instance, filename):
     return f"{instance}-{filename}"



class usuario(models.Model):
     senha = models.CharField(max_length=255)
     nome = models.TextField(max_length=255)
     email = models.EmailField()


class endereco(models.Model):
     rua = models.TextField(max_length=255)
     numero = models.CharField(max_length=255)

class denuncia(models.Model):
     cidade = models.CharField(max_length=255, null=True, blank=True)
     telefone = models.CharField(max_length=255, null=True, blank=True)
     rua = models.CharField(max_length=255, null=True, blank=True)
     pr = models.CharField(max_length=255, null=True, blank=True)
     den = models.TextField(max_length=255, null=True, blank=True)
     image = models.ImageField(upload_to=upload_image, blank=True, null=True)

class suporte(models.Model):
     sup = models.TextField(max_length=255)

