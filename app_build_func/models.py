from django.db import models
from django.utils.safestring import mark_safe


def img_folder(instance, filename):
    filename = str(instance.id) + '.png'
    return "graphics/{}".format(filename)          # где сохранится (создастся папка для этого)


class ModelingFunction(models.Model):
    """Модель моделирования функции"""
    class Meta:
        verbose_name = "График функции"
        verbose_name_plural = "Графики функций"

    function_name = models.CharField(verbose_name="Функция", max_length=300,
                                     help_text="Доступные функции: sqrt, tan, atan, sin, asin, cos, acos. "
                                               "Доступные операции: +,-,/,*,^"
                                               "Разделитель для десятичных дробей - .")
    graphic = models.ImageField(verbose_name="График", upload_to=img_folder, blank=True)
    interval = models.DecimalField(verbose_name="Интервал t, дней", max_digits=12, decimal_places=0,
                                   help_text="Предел: 999999.999999")
    step = models.DecimalField(verbose_name="Шаг t, часы", max_digits=10, decimal_places=0,
                               help_text="Предел: 99999.99999")
    date_treatment = models.DateTimeField(verbose_name="Дата обработки", null=True, blank=True, auto_now=True)

    def __str__(self):
        return f"{self.function_name}"

    def display_graphic(self):
        return mark_safe(f"<img style='width: 400px' src='{self.graphic.url}'>")
    display_graphic.allow_tags = True
    display_graphic.short_description = 'График'
