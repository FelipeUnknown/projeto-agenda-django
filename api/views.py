from django.shortcuts import render
from rest_framework import generics, viewsets

from api.models import Pessoa
from api.serializers import PessoaSerializer

#API v1

class PessoaListarCriarView(generics.ListCreateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class PessoaEditarBuscarDeletarView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

#API v2


class PessoaView(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer