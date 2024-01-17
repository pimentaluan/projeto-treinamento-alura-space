from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form.cleaned_data["nome_login"]
            senha = form.cleaned_data["senha"]

            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha,
            )
            if usuario is not None:
                auth.login(request, usuario)
                return redirect('index')
            else:
                return redirect('login')

    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form.cleaned_data["senha_1"] != form.cleaned_data["senha_2"]:
                return redirect('cadastro')

            nome = form.cleaned_data["nome_cadastro"]
            email = form.cleaned_data["email"]
            senha = form.cleaned_data["senha_1"]

            if User.objects.filter(username=nome).exists():
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            return redirect('login')

    return render(request, "usuarios/cadastro.html", {"form": form})
