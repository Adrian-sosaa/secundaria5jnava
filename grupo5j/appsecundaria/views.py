from django.shortcuts import render
from models import AlumnoT,frase

# Create your views here.

def Index_vista(request):
    misalumnos=AlumnoT.objects.all().order_by("id")
    return render(request,"index.html",{"objeto":misalumnos})
