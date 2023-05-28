from django.contrib import admin

from fisioterapeutas.models import Especialidade, Fisioterapeuta, Agenda

class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ['nome']
    
class FisioterapeutaAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 'crefito', 'telefone',
    ]
    
class AgendaAdmin(admin.ModelAdmin):
    list_display = [
        'dia', 'horario'
    ]
    
admin.site.register(Especialidade, EspecialidadeAdmin)
admin.site.register(Fisioterapeuta, FisioterapeutaAdmin)
admin.site.register(Agenda, AgendaAdmin)