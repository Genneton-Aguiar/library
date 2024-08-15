from rest_framework import viewsets
from django.shortcuts import render
from rest_framework.response import Response
from django.http  import JsonResponse

from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_200_OK,
    HTTP_204_NO_CONTENT
)

from .models import Livros, Autor, Usuario, Emprestimos
from .serializers import LivrosSerializer, AutorSerializer, UsuarioSerializer, EmprestimosSerializer


    
    
class LivrosViewSet(viewsets.ModelViewSet):
    queryset = livros.objects.all()
    serializer_class = LivrosSerializer
    
    def list(self, request, *args, **kwargs):
        
        livro = livros.objects.all()
        serializer= LivrosSerializer(livro, many=True)
        
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        
        data=request.data
        if not data:
            return JsonResponse('infrome o livro',status=HTTP_400_BAD_REQUEST)
        
        titulo=request.data.get('titulo')
        autor=request.data.get('autor')
        editora=request.data.get('editora')
        ano=request.data.get('ano')
        
        criation=livros.objects.create(
            titulo=titulo, 
            autor=autor, 
            editora=editora, 
            ano=ano)
        
        serializer=self.get_serializer(criation)
        hearders=self.get_success_headers(serializer.data)

        return Response(serializer.data, status=HTTP_201_CREATED, headers=hearders)

    def partial_update(self, request, *args, **kwargs):  
        
        titulo=request.data.get('titulo')
        if not  titulo:
            return JsonResponse('infrome o livro',status=HTTP_400_BAD_REQUEST)
        
        pk=self.kwargs.get('pk', None)
        editor=livros.objects.filter(pk=pk).update(
            titulo=titulo
        )
        livro = livros.objects.filter(id=editor).first()
        
        serializer=LivrosSerializer(livro, many=False)
        
        return JsonResponse(serializer.data, status=HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        
        livros=self.get_object()
        livros.delete()
    
        return Response([], status=HTTP_204_NO_CONTENT)
    
class AutorViewSet(viewsets.ModelViewSet):
    queryset = autor.objects.all()
    serializer_class = AutorSerializer
    def list(self, request, *args, **kwargs):
        
        list=autor.objects.filter('nome')
        serializer= AutorSerializer(list, many=True)
        serializer.is_valid(raise_exception=True)
        
        return Response(serializer.data)

    def create(self, request, *args, **kwargs): 
        
        data=request.data
        if not data:
            return JsonResponse('infrome o autor',status=HTTP_400_BAD_REQUEST)
        
        nome=request.data.get('nome')
        nascimento=request.data.get('nascimento')
        
        criation=autor.objects.create(
            nome=nome, 
            nascimento=nascimento)
        
        serializer=self.get_serializer(criation)
        hearders=self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTP_201_CREATED, headers=hearders)

    def partial_update(self, request, *args, **kwargs):
        request.data.is_valid(raise_exception=True)
        
        nome=request.data.get('nome')
        if not  nome:
            return JsonResponse('infrome o autor',status=HTTP_400_BAD_REQUEST)
        
        nascimento=request.data.get('nascimento')
        if not  nascimento:
            return JsonResponse('infrome o autor',status=HTTP_400_BAD_REQUEST)
        
        pk=self.kwargs.get('pk', None)
        
        editor=autor.objects.filter(pk=pk).frits().update(
            nome=nome,
            nascimento=nascimento
            )
        
        serializer=AutorSerializer(editor, many=True)
        serializer.is_valid(raise_exception=True)
        if not serializer.is_valid:
            return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
        return JsonResponse(serializer.data, status=HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):    
        data=request.data.get('nome')
        if not data:
            return JsonResponse('necessário informar nome do autor',status=HTTP_400_BAD_REQUEST)
        
        autor=self.get_object()
        autor.delete()
        
    
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = UsuarioSerializer
    def list(self, request, *args, **kwargs):
        
        list=usuario.objects.filter(is_staff=False)
        serializer= UsuarioSerializer(list, many=True)
        serializer.is_valid(raise_exception=True)
        
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        
        data=request.data
        if not data:
            return JsonResponse('necessário informação do usuario',status=HTTP_400_BAD_REQUEST)
        
        nome=request.data.get('nome')
        email=request.data.get('email')
        nascimento=request.data.get('nascimento')
        is_saff=request.data.get('is_saff')
        
        criation=usuario.objects.create(
            nome=nome, 
            email=email, 
            nascimento=nascimento,
            is_saff=is_saff,
            )
        
        serializer=self.get_serializer(criation)
        hearders=self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTP_201_CREATED, headers=hearders)

    def partial_update(self, request, *args, **kwargs):
        request.data.is_valid(raise_exception=True)
        
        nome=request.data.get('nome')
        if not  nome:
            return JsonResponse('infrome o nome do usuario',status=HTTP_400_BAD_REQUEST)
        
        pendente=request.data.get('pendente')
        if not  pendente:
            return JsonResponse('infrome se o usuario é pendente',status=HTTP_400_BAD_REQUEST)
        
        is_staff=request.data.get('is_staff')
        if not  is_staff:
            return JsonResponse('informe se o usuario é funcionário',status=HTTP_400_BAD_REQUEST)
        
        pk=self.kwargs.get('pk', None)
        
        editor=usuario.objects.filter(pk=pk).frits().update(
            nome=nome,
            pendente=pendente,
            is_taff=is_staff,
            )
        
        serializer=UsuarioSerializer(editor, many=True)
        serializer.is_valid(raise_exception=True)
        if not serializer.is_valid:
            return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
        return JsonResponse(serializer.data, status=HTTP_200_OK)


    def destroy(self, request, *args, **kwargs):
        
        pendente=usuario.objects.filter(nome__pendente=True)
        if pendente:
            return JsonResponse('Não é permitido excluir usuario com pendencia',status=HTTP_401_UNAUTHORIZED)
        
        
        usuario=self.get_object()
        usuario.delete()


class EmprestimosViewSet(viewsets.ModelViewSet):
    queryset = emprestimos.objects.all()
    serializer_class = EmprestimosSerializer

    def list(self, request, *args, **kwargs): 
        
           
        list=emprestimos.objects.filter(usuario__is_staff=False)
        serializer= EmprestimosSerializer(list, many=True)
        serializer.is_valid(raise_exception=True)
        
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        
        titulo=request.data.get('titulo')
        if not  titulo: 
            return JsonResponse('infrome o titulo do livro',status=HTTP_400_BAD_REQUEST)
        
        usuario=request.data.get('usuario')
        if not  usuario:
            return JsonResponse('infrome o usuario',status=HTTP_400_BAD_REQUEST)
        
        criation=emprestimos.objects.create(
            titulo=titulo, 
            usuario=usuario
            )
        
        serializer=self.get_serializer(criation)
        hearders=self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTP_201_CREATED, headers=hearders)
    
    def partial_update(self, request, *args, **kwargs):
        request.data.is_valid(raise_exception=True)
        
        pendente=request.data.get('pendente')  
        if not  pendente:
            return JsonResponse('infrome se o emprestimo é pendente',status=HTTP_400_BAD_REQUEST)
        
        pk=self.kwargs.get('pk', None)
        
        editor=emprestimos.objects.filter(pk=pk).frits().update(
            pendente=pendente
            )
        
        serializer=EmprestimosSerializer(editor, many=True)
        serializer.is_valid(raise_exception=True)
        if not serializer.is_valid:
            return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
        return JsonResponse(serializer.data, status=HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        
        data=request.data.get('nome')
        if not data:
            return JsonResponse('necessário informar nome do usuario',status=HTTP_400_BAD_REQUEST)
        
        pendente=usuario.objects.filter(nome__pendente=True)
        if pendente:
            return JsonResponse('Não é permitido excluir usuario com pendencia',status=HTTP_401_UNAUTHORIZED)
        
        emprestimos=self.get_object()
        emprestimos.delete()
        
    


