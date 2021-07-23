from django.shortcuts import render
from .models import product

# Create your views here.

def index(request):
    item = product.objects.all()
    return render(request, 'store/index.html', {'item':item})