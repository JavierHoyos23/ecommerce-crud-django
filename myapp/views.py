from django.shortcuts import get_object_or_404,render, redirect
from django.http import HttpResponse, HttpResponseForbidden #Importar para regresar respuestas http
from .models import Product
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return HttpResponse('Hello there')

def products(request):
    page_obj = products = Product.objects.all()
    product_name = request.GET.get('product_name')
    if product_name != '' and product_name is not None:
        page_obj = products.filter(name__icontains=product_name)
    paginator = Paginator(page_obj,3) # Para paginacion usando funciones
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj} # Para ingresar el contenido dinamico al template.
    return render(request,'index.html', context)

# Class based view para la vista de productos (ListView)
class ProductListView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'
    paginate_by = 3 # Para paginacion

def product_detail(request,id): #Le pasamos el id del producto.
    product = Product.objects.get(id=id)
    context = {'product':product,}
    return render(request, 'detail.html', context)

# Class based view para la vista del detalle de los productos (DetailView)
class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail.html'
    context_object_name = 'product'

@login_required
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name') # Lleva el nombre del (nombre, id) en el template del formulario.
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload'] # Para imagenes
        seller_name = request.user
        product = Product(name=name, price=price, desc=desc, image=image, seller_name=seller_name)
        product.save()
    return render(request, 'addproduct.html')

# Class based view para la vista de agregar los productos (CreateView)
class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price', 'desc','image','seller_name']
    # Automaticamente linkea a este template product_form.html

@login_required
def update_product(request,id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.desc = request.POST.get('desc')
        if 'upload' in request.FILES and request.FILES['upload']:
            product.image = request.FILES['upload']
        product.save()
        return redirect('/products',)
    context = {'product':product}
    return render(request, 'updateproduct.html', context=context)

# Class based view para la vista de agregar los productos (UpdateView)
class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'price', 'desc','image','seller_name']
    template_name_suffix = '_update_form'

@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, id=id) # Para buscar el objeto y validar al usuario
    # product = Product.objects.get(id=id)
    if product.seller_name != request.user: # validacion del usuario
        return HttpResponseForbidden("No tienes permiso para eliminar este producto.")
    context = {'product' : product,}
    if request.method == 'POST':
        product.delete()
        return redirect('/products')
    return render(request, 'deleteproduct.html', context)

# Class based view para la vista de agregar los productos (DeleteView)
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('myapp:products')

@login_required
def my_listing(request):
    products = Product.objects.filter(seller_name=request.user) #Filtrar los productos que son creados por el usuario
    context = {'products':products}
    return render(request, 'mylistings.html', context)