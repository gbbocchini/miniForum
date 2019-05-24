from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CriaUsuario

# Create your views here.
class Cadastro(CreateView):
    form_class = CriaUsuario
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'