from rest_framework import routers
from django.urls import path, include

from core.views import(
    LivrosViewSet,
    AutorViewSet,
    EmprestimosViewSet,
)

router = routers.DefaultRouter()
router.register(r'livros', LivrosViewSet, basename='livros')
router.register(r'autor', AutorViewSet)
router.register(r'emprestimos', EmprestimosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]   
