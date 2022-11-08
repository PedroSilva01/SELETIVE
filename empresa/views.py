from django.shortcuts import render
from django.http import HttpResponse
from .models import Tecnologia

# Create your views here.
def nova_empresa(request):
    if request.method == "GET":
        techs = Tecnologia.objects.all()
        return render(request, 'nova_empresa.html', {'techs': techs})
    elif request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        cidade = request.POST.get('cidade')
        endereco = request.POST.get('endereco')
        nicho = request.POST.get('nicho')
        tecnologias = request.POST.getlist('tecnologias')
        caracteristicas = request.POST.get('caracteristicas')
        logo = request.FILES.get('logo')
        return HttpResponse("To aqui")
