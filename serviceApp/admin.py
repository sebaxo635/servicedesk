from django.contrib import admin
from serviceApp.models import Alumno , Funcionario , Equipo , Prestamo , Mantencion , Reserva

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ("nombre" , "rut" , "apellido" , "curso")


class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ("nombre" , "rut" , "apellido" , "departamento")


class EquipoAdmin(admin.ModelAdmin):
    list_display = ("marca" , "id_Equipo" , "modelo" , "especificaciones")

class PrestamoAdmin(admin.ModelAdmin):
    list_display = ("id_prestamo" , "id_equipo" )

class MantencionAdmin(admin.ModelAdmin):
    list_display = ("id_ticket", "rut" , "problema_mantencion" , "fecha_mantencion" )
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("rut" , "fecha_reserva" )



# Register your models here.
admin.site.register(Alumno , AlumnoAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Prestamo , PrestamoAdmin)
admin.site.register(Mantencion , MantencionAdmin)
admin.site.register(Reserva , ReservaAdmin)

#ticket mostrar al reves 
