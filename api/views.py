from django.utils.decorators import method_decorator
from rest_framework import generics, viewsets
from rest_framework.mixins import ListModelMixin

from .models import Project
from .serializers import ProjectSerializer, ProjectUpdateSerializer

from ipdb import set_trace


class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    lookup_field = "name"

    def get_serializer_class(self):
        if self.action == "update" or self.action == "partial_update":
            return ProjectUpdateSerializer

        return ProjectSerializer

    def list(self, request, *args, **kwargs):
        """
        Retornar uma lista de todos os projetos.

        Parâmetros: nenhum parâmetro solicitado na URL.
        """
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Retornar um projeto pelo nome.

        Parâmetros: name(str) nome do projeto solicitado na URL.
        """
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Criar um novo projeto.

        Parâmetros: nenhum parâmetro solicitado na URL.
        """
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Alterar apenas o nome de um projeto.

        Parâmetros: name(str) nome do projeto solicitado na URL.
        """
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Alterar apenas o nome de um projeto.

        Parâmetros: name(str) nome do projeto solicitado na URL.
        """
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Deletar um projeto pelo nome.

        Parâmetros: name(str) nome do projeto solicitado na URL.
        """
        return super().destroy(request, *args, **kwargs)
