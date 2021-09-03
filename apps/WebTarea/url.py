from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('Pagina-siguiente', Pagina_siguiente, name='Pagina-siguiente'),

]
