from django.contrib.auth import views as authentication_views
from django.contrib import admin
from django.urls import path
from . import views #importar las vistas del archivo de la app.


app_name = 'users' # Name spacing para evitar colisiones.

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', authentication_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('createprofile/', views.create_profile, name='createprofile'),
    path('sellerprofile/<int:id>', views.seller_profile, name='sellerprofile'),
]
