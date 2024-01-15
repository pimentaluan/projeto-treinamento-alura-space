from django.urls import path
from usuarios.views import login, cadastro

urlpatterns = [
    path('login', login, name='login'),
    cadastro('cadastro', cadastro, name='cadastro'),
]