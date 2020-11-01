from django.db import models

# Create your models here.


class ModelingFunction(models.Model):
    function_name = models.CharField(verbose_name="Функция", max_length=300, help_text="Введите в поле функцию.")
    graphic = models.ImageField()
    interval = models.DecimalField

