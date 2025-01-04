from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('registrarCurso/', views.registrarCurso, name='registrarCurso'),
    path('edicionCurso/<codigo>', views.edicionCurso, name='edicionCurso'),
    path('editarCurso/', views.editarCurso, name='editarCurso'),
    path('eliminarCurso/<codigo>', views.eliminarCurso, name='eliminarCurso'),
]