from django.contrib import admin
# Importar el mismo nombre que esta en admin.py
from EmpleadosApp.models import Empleados

# Register your models here.


class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'salario',
                    'departamento', 'fecha_contratacion']


admin.site.register(Empleados, EmpleadosAdmin)

# Register your models here.
