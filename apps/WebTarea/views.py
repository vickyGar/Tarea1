from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def Pagina_siguiente(request):
    return render(request, 'Pagina-siguiente.html')

