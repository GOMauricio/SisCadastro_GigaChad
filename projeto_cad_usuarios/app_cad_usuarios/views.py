from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios (request):

    # Solicitar e salvar usuários
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    # Exibir usuários já cadastrados
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    # Retornar dados para a página de listagem
    return render(request, 'usuarios/usuarios.html', usuarios)
