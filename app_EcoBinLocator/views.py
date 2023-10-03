from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import usuario, endereco, denuncia, suporte




def pagina_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        # Lógica de autenticação (se necessário)

    return render(request, 'usuarios/login.html')


def pagina_cadastro(request):
    if request.method == 'POST':
        # Obtenha os dados do formulário
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        # Crie um novo objeto Usuario e tente salvá-lo no banco de dados
        novo_usuario = usuario(nome=nome, email=email, senha=senha)
        novo_usuario.save()
        
        # Redirecione o usuário para a página de login após o cadastro bem-sucedido
        return redirect('pagina_login')  # Redirecione para a página de login após o cadastro e login

    return render(request, 'usuarios/cadastro.html')




def pagina_home(request):
    # Coloque aqui o código necessário para renderizar a página home.html
    return render(request, 'usuarios/home.html')


def pagina_denuncia(request):
    if request.method == 'POST':
        den = request.POST.get('denuncia')
        rua = request.POST.get('rua')
        cidade = request.POST.get('cidade')
        pr = request.POST.get('pr')
        telefone = request.POST.get('telefone')

        nova_denuncia = denuncia(den= den, rua=rua, cidade=cidade, pr=pr, telefone=telefone)
        nova_denuncia.save()

        return redirect('pagina_home')
    # Coloque aqui o código necessário para renderizar a página de denúncia
    return render(request, 'usuarios/denuncia.html')


def pagina_suporte(request):
    if request.method == 'POST':
        sup = request.POST.get("sup")

        novo_sup = suporte(sup=sup)
        novo_sup.save()
        return redirect('pagina_home')
    # Coloque aqui o código necessário para renderizar a página de denúncia
    return render(request, 'usuarios/suporte.html')


def pagina_instrucoes(request):
    # Coloque aqui o código necessário para renderizar a página de denúncia
    return render(request, 'usuarios/instrucoes.html')


def pagina_endereco(request):
    if request.method == 'POST':
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')
        
        novo_end = endereco(rua=rua, numero=numero)
        novo_end.save()
        
        return redirect('pagina_home')
    # Coloque aqui o código necessário para renderizar a página de denúncia
    return render(request, 'usuarios/endereco.html')


def pagina_mapa(request):
    # Coloque aqui o código necessário para renderizar a página de denúncia
    return render(request, 'usuarios/mapa.html')