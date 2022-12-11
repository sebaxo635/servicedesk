from django.db import models

# Create your models here.

class Usuario(models.Model):
    rut = models.CharField(max_length=12 , primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField(max_length=30 , unique=True)
    
    def __str__(self) :
        return self.rut
    
    
    class Meta:
        abstract = True

class Alumno(Usuario):
    curso = models.CharField(max_length=15)
    
class Funcionario(Usuario):
    departamento = models.CharField(max_length=15)
    
class Preguntas(models.Model):
    problemapregunta = models.TextField(max_length=1000 , default="disco")
    solucion = models.CharField(max_length=1000 )
    
class Equipo(models.Model):
    id_Equipo = models.CharField(primary_key=True , max_length=5)
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=15 )
    especificaciones = models.TextField(max_length=150 )
    proveedor = models.CharField( max_length=30)
    detalles = models.TextField(max_length=150 )
    fecha_compra = models.DateField()
    def __str__(self) :
        return self.id_Equipo
    

class Prestamo(models.Model):
    id_prestamo = models.AutoField(primary_key=True  )
    fecha_despacho = models.DateField( auto_now_add=True )
    id_equipo = models.ForeignKey(Equipo , on_delete=models.CASCADE , default=1)
    rut = models.ForeignKey(Alumno , on_delete=models.CASCADE , default="" )
    
class Ticket(models.Model):
    id_ticket = models.BigAutoField(primary_key=True)
    

    
    class meta:
        abstract = True
        ordering = ['id_ticket']
    
class Mantencion(Ticket):
    
    rut = models.ForeignKey(Alumno , on_delete=models.CASCADE , default="" )
    problema_mantencion = models.TextField(max_length=150 , default="")
    fecha_mantencion= models.DateField(auto_now=True)
    
class Reserva(Ticket):
    
    rut = models.ForeignKey(Alumno , on_delete=models.CASCADE , default="" )
    fecha_reserva = models.DateField(auto_now=True)
    
    