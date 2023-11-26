from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import endereco, denuncia, suporte
from django.core.files.storage import FileSystemStorage
from django.conf import settings




def pagina_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        usuario = authenticate(request, email = email, password= senha)
        print(usuario, email, senha)
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else:
            messages.error (request, 'Email ou senha incorretos')
            return redirect('home')
    return render(request, 'usuarios/login.html')


def pagina_cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        meu_usuario = User.objects.create_user(nome, email, senha)
        meu_usuario.save()
        return redirect('login') 
        
        

    return render(request, 'usuarios/cadastro.html')




def pagina_home(request):
    return render(request, 'usuarios/home.html')


def pagina_denuncia(request):
    if request.method == 'POST':
        den = request.POST.get('denuncia')
        rua = request.POST.get('rua')
        cidade = request.POST.get('cidade')
        pr = request.POST.get('pr')
        telefone = request.POST.get('telefone')
        image = request.FILES.get('image')

        if image:
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            
            filename = fs.save(image.name, image)
            
            image_url = fs.url(filename)

        nova_denuncia = denuncia(den= den, rua=rua, cidade=cidade, pr=pr, telefone=telefone, image=image)
        nova_denuncia.save()

        return redirect('home')
    return render(request, 'usuarios/denuncia.html')


def pagina_suporte(request):
    if request.method == 'POST':
        sup = request.POST.get("sup")

        novo_sup = suporte(sup=sup)
        novo_sup.save()
        return redirect('home')
    return render(request, 'usuarios/suporte.html')


def pagina_instrucoes(request):
    return render(request, 'usuarios/instrucoes.html')


def pagina_produtos(request):
    return render(request, 'usuarios/produtos.html')


def pagina_endereco(request):
    if request.method == 'POST':
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')
        
        novo_end = endereco(rua=rua, numero=numero)
        novo_end.save()
        
        return redirect('home')
    return render(request, 'usuarios/endereco.html')


def pagina_mapa(request):
    return render(request, 'usuarios/mapa.html')


def pagina_checklist(request):
    return render(request, 'usuarios/checklist.html')