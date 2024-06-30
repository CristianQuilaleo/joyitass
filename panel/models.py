from django.db import models
from django.contrib.auth.models import User
from .models import Carrito, Producto

# Create your models here.

class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True, db_column='idGenero')
    genero = models.CharField(max_length=20,blank=False,null=False)

    def __str__(self):
        return str(self.genero)
    

class Cliente(models.Model):
    id_cliente       = models.AutoField(primary_key=True)
    rut              = models.CharField(max_length=10)
    nombre_cl        = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    id_genero        = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')  
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion        = models.CharField(max_length=100, blank=True, null=True)  
    contrasena       = models.CharField(max_length=50, blank=False, null=False)
    
    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)
    
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_prod = models.CharField(max_length=30)
    descripcion = models.TextField()
    precio      = models.IntegerField()  
    stock       = models.IntegerField()

    def __str__(self):
        return self.nombre_prod

class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
         return f"Carrito de {self.usuario.username}"

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def subtotal(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre_prod} en {self.carrito.usuario.username}'s Carrito"