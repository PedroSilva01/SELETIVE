from django.shortcuts import render
from django.http import HttpResponse
from .models import Tecnologia, Empresa
from django.shortcuts import redirect

# Create your views here.
def nova_empresa(request):
    if request.method == "GET":
        techs = Tecnologia.objects.all()
        return render(request, 'nova_empresa.html', {'techs': techs})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cidade = request.POST.get('cidade')
        endereco = request.POST.get('endereco')
        nicho = request.POST.get('nicho')
        tecnologias = request.POST.getlist('tecnologias')
        caracteristicas = request.POST.get('caracteristicas')
        logo = request.FILES.get('logo')
        if (len(nome.strip()) == 0 or len(email.strip()) == 0 or len(cidade.strip()) == 0):
            return redirect('/home/nova_empresa')
        return HttpResponse("To aqui")
