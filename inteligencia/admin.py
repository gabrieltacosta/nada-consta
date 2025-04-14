from django.contrib import admin
from .models import PostGrad, Policial

@admin.register(PostGrad)
class PostGradAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    list_filter = ("title",)

@admin.register(Policial)
class PolicialAdmin(admin.ModelAdmin):
    list_display = ("conduta", "post_grad", "re", "nome_guerra", "nome_completo", "opm", "subunidade", "situacao", "Consulta", "P2", "JD", "Observação", "updated_at")
    search_fields = ("re", "nome_guerra", "consulta", "p2", "jd")
    list_filter = ("conduta", "post_grad", "opm", "subunidade")
    list_display_links = ('re',)
    ordering = ('post_grad',)
