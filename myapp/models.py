from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Product(models.Model): #Los modelos sirven para crear las tablas en la bd.
    #El id es creado automaticamente por Django.
    seller_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='images') # Para agregar imagenes se requiere lib pillow
    

    def __str__(self): 
        return self.name
    
    def get_absolute_url(self): # Redirige cuando se usa class formularios (Create, Update, Delete) es necesario.
        return reverse('myapp:products')
