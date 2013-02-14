from principal.models import Receta, Comentario
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext


def sobre(request):
    html = '<html><body><h1>Este es el titulo</h1><p>Por aca va el contenido</p></body></html>'
    return HttpResponse(html)


def inicio(request):
    recetas = Receta.objects.all()
    return render_to_response('inicio.html', {'recetas': recetas})


def usuarios(request):
    usuarios = User.objects.all()
    recetas = Receta.objects.all()
    return render_to_response('usuarios.html', {'usuarios': usuarios, 'recetas': recetas})


def lista_recetas(request):
    recetas = Receta.objects.all()
    return render_to_response('recetas.html', {'datos': recetas}, context_instance=RequestContext(request))
