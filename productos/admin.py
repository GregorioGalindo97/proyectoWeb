from django.contrib import admin
from .models import CategoriaProd, Producto

class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

class ProductosAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

admin.site.register(CategoriaProd,ProductosAdmin)
admin.site.register(Producto,ProductosAdmin)
