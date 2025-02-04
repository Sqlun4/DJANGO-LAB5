from django.shortcuts import render
from .forms import RegistroUsuariosForm

# Create your views here.
def registro (request):
    if request.method == "POST":
        form = RegistroUsuariosForm(request.POST)
        if form.is_valid():
            return render(request,'usuarios/registro_exitoso.html')

    else:
        form = RegistroUsuariosForm()

    return render(request, 'usuarios/registro.html', {'form':form})

