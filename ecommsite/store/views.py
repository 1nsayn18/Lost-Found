from django.core import paginator
from django.shortcuts import render
from .models import product
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    item = product.objects.all()

    #search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        item = item.filter(name__icontains = item_name)     

    #paginator code
    paginator = Paginator(item, 4)
    page = request.GET.get('page')
    item = paginator.get_page(page)

    return render(request, 'store/index.html', {'item':item})

def detail(request, id):
    item = product.objects.get(id=id)

    return render(request, 'store/detail.html', {'item':item})