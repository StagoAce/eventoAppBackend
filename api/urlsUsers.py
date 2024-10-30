from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Asegúrate de que la vista index exista
    path('all/', views.get_all_users, name='get_all_users'),  # Un endpoint para obtener todos los usuarios
    path('add/', views.add_user, name='add_user'),  # Un endpoint para añadir un usuario
    path('<int:user_cedula>', views.get_user, name='get_user'),
    path('eventos/<int:user_cedula>', views.get_eventos_user, name='get_user'),
    path('login', views.validate_user, name="validate_user"),
    path('subscribe/<int:user_cedula>', views.subscribe_evento, name="subscribe_evento"),
    path('unsubscribe/<int:user_cedula>', views.unsubscribe_evento, name="unsubscribe_evento"),
]