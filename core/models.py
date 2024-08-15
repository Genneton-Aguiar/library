from django.db import models

class Autor (models.Model):

   nome=models.CharField(
      max_length=100,
   )

   nascimento= models.DateTimeField(
      verbose_name="data de nascimento do autor",
      blank=True,
      null=True,
   )


class Categoria(models.Model):
   nome = models.CharField(max_length=255)

   def __str__(self):
       return self.nome


class Livros(models.Model):

   titulo=models.CharField(
      verbose_name="titulos",
      max_length=100,
      blank=False,
      null=False,
   )
   categoria=models.ForeignKey(
      Categoria,
      on_delete=models.PROTECT
   )

   editora=models.CharField(
      verbose_name = "editoras",
      max_length=100,
      blank=False,
      null=False,
   )

   ano=models.DateTimeField(
      verbose_name="ano do livro",
      blank=False,
      null=True,
   )

   disponibilidade = models.BooleanField(
      blank=False,
      null=True,
   )

   autor=models.ForeignKey( 
      Autor,
      verbose_name="autor do livro",
      on_delete=models.PROTECT,
      blank=True,
      null=True,
   )  


class Usuario(models.Model):

   nome=models.CharField(
      verbose_name="nome do usuario",
      max_length=100,
      blank=True,
      null=False,
   )

   email=models.CharField(
      max_length=100,
      blank=True,
      null=False,
   )

   nascimento=models.DateTimeField(
      blank=True,
      null=True,
   )

   is_staff= models.BooleanField(
      verbose_name ="usuario é funcionario?",
      blank=True,
      null=True,
   )

   pendente=models.BooleanField(
      blank=False,
      null=True,
   )

   emprestimo= models.DateTimeField(
      blank=True,
      null=True,
   )

   devolução=models.DateTimeField(
      blank=True,
      null=True,
   )


class Emprestimos(models.Model):

   livro = models.ForeignKey(
      Livros,
      on_delete=models.PROTECT
   )
   usuario=models.ForeignKey(
      Usuario,
      on_delete=models.PROTECT
   )




 

