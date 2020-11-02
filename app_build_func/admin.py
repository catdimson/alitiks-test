from django.contrib import admin
from .models import ModelingFunction
from .tasks import paint_graphic


@admin.register(ModelingFunction)
class ModelingFunctionAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("custom.css",)
        }

    readonly_fields = ("date_treatment",)
    actions_selection_counter = False
    list_display = ("function_name", "display_graphic", "interval", "step", "custom_date")

    def custom_date(self, obj):
        return obj.date_treatment.strftime('%Y-%m-%d %H:%M:%S.%f')
    custom_date.short_description = "Дата обработки"

    def save_model(self, request, obj, form, change):
        paint_graphic(obj, change)
        # obj.user = request.user
        # print(obj.function_name)
        # print(obj.interval)
        # print(obj.step)
        # print(obj.id)
        super().save_model(request, obj, form, change)