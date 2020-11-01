# Generated by Django 3.1.2 on 2020-11-01 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelingFunction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('function_name', models.CharField(help_text='Введите в поле функцию.', max_length=300, verbose_name='Функция')),
                ('graphic', models.ImageField(upload_to='')),
                ('interval', models.DecimalField(decimal_places=6, help_text='Предел: 999999.999999', max_digits=12, verbose_name='Интервал')),
                ('step', models.DecimalField(decimal_places=5, help_text='Предел: 99999.99999', max_digits=10, verbose_name='Шаг')),
                ('date_treatment', models.DateTimeField(verbose_name='Время обработки')),
            ],
        ),
    ]
