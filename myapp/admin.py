from django.contrib import admin
from .models import Product

# Register your models here.
admin.site.site_header = 'Buy and Sell Website' # Cambiar header
admin.site.site_title = 'Website'
admin.site.index_title = 'Manage Website'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','desc') # Desplegar mas info
    search_fields = ('name',) # Agregar parametro de busqueda

    def set_price_to_zero(self, request, queryset): # Se crea accion admin personalizada
        queryset.update(price=0)

    actions = ('set_price_to_zero',) #Establecer acciones de admin personalizada

admin.site.register(Product, ProductAdmin) # Se le pasan los parametros personalizados