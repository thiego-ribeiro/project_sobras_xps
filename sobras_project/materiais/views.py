from django.shortcuts import render, redirect, get_object_or_404
from .models import SobraMaterial, ImagemDispositivo
from .forms import SobraMaterialForm, SolicitacaoForm, Solicitacao
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def criar_usuarios_padrao():
    if not User.objects.filter(username='admin@exemplo.com').exists():
        User.objects.create_user(
            username='admin@exemplo.com',
            email='admin@exemplo.com',
            password='123456',
            is_staff=True
        )

    if not User.objects.filter(username='solicitador@exemplo.com').exists():
        User.objects.create_user(
            username='solicitador@exemplo.com',
            email='solicitador@exemplo.com',
            password='123456'
        )

def login(request):
    criar_usuarios_padrao()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            auth_login(request, user)

            if user.is_staff:
                return redirect('lista_sobras')
            else:
                return redirect('solicitar_materiais')

        messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'materiais/login.html')

def base(request):
    return render(request, 'materiais/base.html')

def lista_sobras(request):
    """
    Lista todas as sobras cadastradas com suas imagens.
    """
    sobras = SobraMaterial.objects.all().order_by('-data_registro')
    return render(request, 'materiais/lista.html', {'sobras': sobras})

def cadastrar_sobra(request):
    """
    Cadastra uma nova sobra e suas imagens (múltiplas).
    """
    if request.method == 'POST':
        form = SobraMaterialForm(request.POST)
        imagens = request.FILES.getlist('imagens')

        if form.is_valid():
            sobra = form.save()
            for img in imagens:
                ImagemDispositivo.objects.create(sobra=sobra, imagem=img)
            return redirect('lista_sobras')
    else:
        form = SobraMaterialForm()

    return render(request, 'materiais/cadastrar.html', {'form': form})

def marcar_como_doado(request, id):
    """
    Marca a sobra como 'Doado'.
    """
    sobra = get_object_or_404(SobraMaterial, id=id)
    sobra.status = 'Doado'
    sobra.save()
    return redirect('lista_sobras')

def solicitacoes(request):
    return render(request, 'materiais/solicitacoes.html')

def solicitar_materiais(request):
    if request.method == 'POST':
        form = SolicitacaoForm(request.POST, request.FILES)

        if form.is_valid():
            solicitacao = form.save()

            # pegar imagens
            imagens = request.FILES.getlist('imagens')

            # salvar imagens (precisa de modelo separado se existir)
            for img in imagens:
                ImagemDispositivo.objects.create(
                    solicitacao=solicitacao,
                    imagem=img
                )

            return redirect('solicitacao_sucesso')

    else:
        form = SolicitacaoForm()

    return render(
        request,
        'materiais/solicitar_materiais.html',
        {'form': form}
    )

def solicitacoes(request):
    lista_solicitacoes = Solicitacao.objects.all().order_by('-id')

    return render(
        request,
        'materiais/solicitacoes.html',
        {
            'solicitacoes': lista_solicitacoes
        }
    )

def solicitacao_sucesso(request):
    return render(request, 'materiais/solicitacao_sucesso.html')
