from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Language,Paradigm,Programmer
from .serializers import LanguageSerializer,ParadigmSerializer,ProgrammerSerializer

class LanguageView(viewsets.ModelViewSet):
    queryset=Language.objects.all()
    serializer_class=LanguageSerializer

class ParadigmView(viewsets.ModelViewSet):
    queryset=Paradigm.objects.all()
    serializer_class=ParadigmSerializer

class ProgrammerView(viewsets.ModelViewSet):
    queryset=Programmer.objects.all()
    serializer_class=ProgrammerSerializer
