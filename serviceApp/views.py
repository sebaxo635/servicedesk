from django.shortcuts import render , HttpResponse
from .models import Equipo , Mantencion , Alumno , Reserva , Prestamo
from django.contrib import messages
# Create your views here.

def Ticket_Reserva(request):
    if request.method == "POST":
        fecha = request.POST.get('fecha')
        Rut = request.POST.get('rut')
        if Alumno.objects.filter(rut=Rut).exists():
            Rut = Alumno.objects.get(rut = Rut)
            Reserva.objects.create(  rut = Rut , fecha_reserva = fecha )
            messages.add_message(request=request , level=messages.SUCCESS , message="Ticket de Reserva Registrado Correctamente")
            return render(request , 'preguntas.html')
        else:
            messages.add_message(request=request , level=messages.ERROR , message="Rut incorrecto o No Registrado")
    return render(request, 'reserva.html'  )

def Ticket_Mantencion(request):
    if request.method == "POST":
        Problema = request.POST.get('problema')
        Rut = request.POST.get('rut')
        if Alumno.objects.filter(rut=Rut).exists():
            Rut = Alumno.objects.get(rut = Rut)
            Mantencion.objects.create(problema_mantencion = Problema , rut = Rut )
            messages.add_message(request=request , level=messages.SUCCESS , message="Ticket de Mantencion Registrado Correctamente")
            return render(request , 'preguntas.html')
        else:
            messages.add_message(request=request , level=messages.ERROR , message="Rut incorrecto o No Registrado")
    return render(request , 'mantencion.html')

def Preguntas(request):
    
    return render(request, 'preguntas.html')

def Retiro(request):
    if request.method == "POST":
        fecha = request.POST.get('fecha')
        Rut = request.POST.get('rut')
        codigo = request.POST.get('codigo')
        if Alumno.objects.filter(rut=Rut).exists() and Equipo.objects.filter(id_Equipo = codigo):
            Rut = Alumno.objects.get(rut = Rut)
            codigo = Equipo.objects.get(id_Equipo = codigo)
            Prestamo.objects.create( rut = Rut , fecha_despacho = fecha , id_equipo=codigo )
            messages.add_message(request=request , level=messages.SUCCESS , message="Retiro Registrado Correctamente")
            return render(request , 'preguntas.html')
        else:
            if Alumno.objects.filter(rut=Rut).exists() :
                messages.add_message(request=request , level=messages.ERROR , message="Equipo No Registrado")
            else:
                messages.add_message(request=request , level=messages.ERROR , message="Rut incorrecto o No Registrado ")

    return render(request , 'retiro.html')

def Registro(request):
    if request.method == "POST":
        Modelo = request.POST.get('modeloA')
        Marca = request.POST.get('marca')
        Especificaciones = request.POST.get('especificaciones')
        Detalle = request.POST.get('detalle')
        Id_equipo = request.POST.get('id_equipo')
        Proveedor = request.POST.get('proveedor')
        Fecha_compra = request.POST.get('fecha_compra')
        if Equipo.objects.filter(id_Equipo = Id_equipo).exists():
            messages.add_message(request=request , level=messages.ERROR , message="Id de Equipo ya Registrado ")
        else: 
            Equipo.objects.create(id_Equipo = Id_equipo , marca = Marca , modelo = Modelo ,
                                especificaciones = Especificaciones , proveedor = Proveedor, 
                                detalles = Detalle , fecha_compra = Fecha_compra)
            messages.add_message(request=request , level=messages.SUCCESS , message="Equipo Registrado Correctamente")
            return render(request , 'preguntas.html')
    return render(request , 'registro.html')