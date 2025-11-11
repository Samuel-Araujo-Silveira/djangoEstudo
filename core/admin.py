from django.contrib import admin
from core.models import Categoria, Editora, ItensCompra, Compra, Livro, Autor

admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Livro)
admin.site.register(Autor)

class ItensInLine(admin.TabularInline):
    model = ItensCompra

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = (ItensInLine,)
    