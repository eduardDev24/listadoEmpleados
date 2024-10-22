from django.shortcuts import render
from EmpleadosApp.models import Empleados
# Create your views here.


def empleadosLista(request):
    empleados = Empleados.objects.all()
    data = {'empleados': empleados}
    return render(request, 'index.html', data)
