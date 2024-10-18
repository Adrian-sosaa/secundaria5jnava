from django.contrib import admin
from .models import AlumnoT,frase
# Register your models here.




class ComentarioIntLine(admin.TabularInline):
    model=frase
    extra=1

class AlumnoAdmin(admin.ModelAdmin):
    fields=["apaterno","amaterno","fecha_nacimiento","fecha_ingreso"]
    list_display=["apaterno","amaterno","nombre"]
    inlines=[ComentarioIntLine]

admin.site.register(AlumnoT,AlumnoAdmin)

@admin.register(frase)
class fraseadmin(admin.ModelAdmin):
    fields=["comentario","Alumno_fk"]
    list_display=["comentario"]