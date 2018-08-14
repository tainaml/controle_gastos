from django.db import models





# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now=True)
    comentario = models.ForeignKey(ComentariosGerais, verbose_name=("Comments"),on_delete=models.CASCADE)


    def __str__(self):
        return  self.nome


class Transacao (models.Model):
    data = models.DateTimeField(auto_now=True)
    descricao= models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)



    class Meta:
        verbose_name_plural = 'Transacoes'


    def __str__(self):
        return self.descricao


class ComentariosGerais(models.Model):
    descricao = models.TextField(max_length=200)
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Comentarios Gerais"

    def __str__(self):
        return  self.nome












