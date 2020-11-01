from django.contrib import admin
from .models import ModelingFunction


@admin.register(ModelingFunction)
class ModelingFunctionAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("custom.css",)
        }

    readonly_fields = ("date_treatment",)
    actions_selection_counter = False
    list_display = ("function_name", "graphic", "interval", "step", "date_treatment")
