from django.urls import path
from . import views #importar las vistas del archivo de la app.


app_name = 'myapp' # Name spacing para evitar colisiones.

urlpatterns = [
    path('', views.index),
    path('products/', views.products, name='products'), # Al agregar un name podemos agregar urls dinamicos a los templates.
    #pk significa primary key para cuando se usan Class Views
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'), #Se menciona el tipo de variable que se pasa.
    path('products/add/', views.add_product, name='add_product'),
    path('products/update/<int:id>/',views.update_product, name='update_product'),
    path('products/delete/<int:id>/',views.delete_product, name='delete_product'),
    path('products/mylistings/',views.my_listing, name='mylistings'),
]
