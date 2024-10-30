from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Asegúrate de que la vista index exista
    path('all/', views.get_all_eventos, name='get_all_eventos'),  # Un endpoint para obtener todos los usuarios
    path('add/<int:cedula_cliente>', views.create_evento, name='create_evento'),  # Un endpoint para añadir un usuario
    path('producer/<int:user_cedula>', views.get_all_eventos_by_client, name='get_all_eventos_by_client'),
]
