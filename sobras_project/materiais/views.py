from django.shortcuts import render, redirect, get_object_or_404
from .models import SobraMaterial, ImagemDispositivo
from .forms import SobraMaterialForm

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
