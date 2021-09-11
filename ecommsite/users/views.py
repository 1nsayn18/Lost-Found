from django.shortcuts import render
from .forms import RegistrationForm
# Create your views here.

def register(request):
    if(request.method == 'POST'):
        form = RegistrationForm(request.POST)
        if(form.is_valid):
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']

    form = RegistrationForm() 
    context = {
        'form':form,
    }
    return render(request, 'users/register.html', context)

def login(request):
    return render(request, 'users/login.html')

def logout(request):
    return 