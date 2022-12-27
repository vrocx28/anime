from django.contrib import admin
from .models import Anime_All

# Register your models here.


class GogoanimeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "anime_name",
        "gogoanime_url",
        "gogoanime_id",
        "no_of_episodes",
        "status",
        # "other_name",
        "summary",
    ]
    readonly_fields = ["id"]


admin.site.register(Anime_All, GogoanimeAdmin)
