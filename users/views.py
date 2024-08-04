from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . forms import NewUserForm
from  django.contrib.auth.decorators import login_required
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/products')
    form = NewUserForm()
    context = {'form':form,}
    return render(request, 'register.html', context)

@login_required
def profile(request):
    return render(request, 'profile.html')
                                                                             
@login_required
def create_profile(request):
    if request.method == 'POST':
        contact_number = request.POST.get('contact_number')
        image = request.FILES['upload']
        user = request.user # Para obtener el usuario actual
        profile = Profile(user=user,image=image,contact_number=contact_number)
        profile.save()
    return render(request, 'createprofile.html')

def seller_profile(request, id):
    seller = User.objects.get(id=id)
    context = {'seller':seller}
    return render(request, 'sellerprofile.html', context)
                                                                             