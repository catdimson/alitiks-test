from django.db import models

# Create your models here.


class ModelingFunction(models.Model):
    class Meta:
        verbose_name = "График функции"
        verbose_name_plural = "Графики функций"

    function_name = models.CharField(verbose_name="Функция", max_length=300, help_text="Введите в поле функцию.")
    graphic = models.ImageField(verbose_name="График", blank=True)
    interval = models.DecimalField(verbose_name="Интервал t, дней", max_digits=12, decimal_places=0,
                                   help_text="Предел: 999999.999999")
    step = models.DecimalField(verbose_name="Шаг t, часы", max_digits=10, decimal_places=0, help_text="Предел: 99999.99999")
    date_treatment = models.DateTimeField(verbose_name="Дата обработки", null=True, blank=True)

    def __str__(self):
        return f"{self.function_name}"
