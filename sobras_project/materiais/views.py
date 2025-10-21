from django.shortcuts import render, redirect, get_object_or_404
from .models import SobraMaterial
from .forms import SobraMaterialForm

def lista_sobras(request):
    sobras = SobraMaterial.objects.all().order_by('-data_registro')
    return render(request, 'materiais/lista.html', {'sobras': sobras})

def cadastrar_sobra(request):
    if request.method == 'POST':
        form = SobraMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_sobras')
    else:
        form = SobraMaterialForm()
    return render(request, 'materiais/cadastrar.html', {'form': form})

def marcar_como_doado(request, id):
    sobra = get_object_or_404(SobraMaterial, id=id)
    sobra.status = 'Doado' 
    sobra.save()
    return redirect('lista_sobras')
