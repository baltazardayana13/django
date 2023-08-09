from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseNotFound
from .models import Product
# Create your views here.
#imprime en pantalla el precio y su titulo acompañado de su complemnto en html
#def index(request):
 #   products = Product.objects.all()

  #  for p in products:
   #     print(p)
    
    #return render(request,'index.html', {'products': products})
def index(request):
    page_number =request.GET.get('page')
    #como solo tengo 4 productos creo 2 paginas
    products_page =Paginator(Product.objects.all(),2)
    #con esto obtenemos imformacion si da en pagina 1 o 2
    try:
        products = products_page.get_page(page_number)
    except PageNotAnInteger:
    #Si no es una pagina correcta manda a la pagina 1
        products = products_page.page(1)
    except EmptyPage:
    #Si es una pagina fuera de rango manda a la pagina 1
        products = products_page.page(1)
    #products = products.get_page(1)
    #con get igual a 2 obtengo producto 3 y 4 con 1 prod 1 y 2
    return render(request,'index.html', {'products': products})

def show(request,pk):
    
    #Marque error 404 en pagina no encontrada lo mis mo de arriba diferente manera
    try:
        product=Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        #pagina no valida error 404
        #return HttpResponse(status=404)
        return HttpResponseNotFound()

    return render(request,'show.html', {'product': product})
