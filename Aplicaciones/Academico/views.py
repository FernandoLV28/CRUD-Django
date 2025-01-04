from django.shortcuts import redirect, render
from .models import Curso
from django.contrib import messages

# Create your views here.

def home(request):
    listadoCursos = Curso.objects.all()
    #messages.success(request, '¡Cursos listados con éxito!')
    return render(request, 'gestionCursos.html', {"cursos": listadoCursos})

def registrarCurso(request):
    codigo = request.POST ['txtCodigo']
    nombre = request.POST ['txtNombre']
    creditos = request.POST ['numCreditos']
    
    curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)  # noqa: F841
    
    messages.success(request, '¡Curso registrado con éxito!')
    return redirect('/')

def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})

def editarCurso(request):
    codigo = request.POST ['txtCodigo']
    nombre = request.POST ['txtNombre']
    creditos = request.POST ['numCreditos']
    
    curso = Curso.objects.get(codigo=codigo)
    
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()
    
    messages.success(request, '¡Curso actualizado con éxito!')
    
    return redirect('/')


def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    messages.success(request, '¡Cursos eliminado!')
    return redirect('/')