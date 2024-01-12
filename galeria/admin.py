from django.contrib import admin
from galeria.models import Fotografia


class ListandoNomes(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("categoria",)

admin.site.register(Fotografia, ListandoNomes)