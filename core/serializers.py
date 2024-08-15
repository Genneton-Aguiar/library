from rest_framework import serializers
from .models import livros,autor,usuario,emprestimos



class LivrosSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = livros
        fields = ('id','autor','editora','ano','titulo')


class AutorSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = autor
        fields = '__all__'
        
        
class UsuarioSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = usuario
        fields = '__all__'


class EmprestimosSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = emprestimos
        fields = '__all__'
