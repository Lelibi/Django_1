from django.urls import path
from galeria.views import index

urlpatterns = [
    path('', index, name='index'),  # Certifique-se de que a view 'index' está definida em galeria/views.py
]
