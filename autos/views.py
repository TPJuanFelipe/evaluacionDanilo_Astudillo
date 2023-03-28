from django.shortcuts import render

def inicio(request):
    
    autos=['Autos', 'Marcas','Nombres', 'Modelos','Colores']
    context={'listado':autos}
    return render(request, 'inicio.html', context)
# Create your views here.

def clientes(request):
    clientes=['Nombres', 'Apellidos','Direccion', 'email', 'Telefono']
    context={'listado':clientes}
    return render(request, 'clientes.html', context)
