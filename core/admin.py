from django.contrib import admin
from .models import livros, autor, usuario, emprestimos 



admin.site.register(livros)
admin.site.register(autor)
admin.site.register(usuario)
admin.site.register(emprestimos)