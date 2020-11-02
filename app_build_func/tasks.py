from test_work.celery import app
from test_work import settings
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from django.core.files.images import ImageFile


# @app.task
def paint_graphic(obj, change):
    """Функция отрисовки графика"""
    func = validate_func(obj.function_name)
    end = datetime.now()
    start = (end - timedelta(days=int(obj.interval))).hour
    end = end.hour
    x = [-3, -2, -1, 0, 1, 2, 3]
    y = [9, 4, 1, 0, 1, 4, 9]
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.grid()
    fig.savefig(settings.MEDIA_ROOT + f"/mpl/{obj.id}.png")

    if change:
        print("Изменяется")
        obj.graphic = ImageFile(open(settings.MEDIA_ROOT + f"/mpl/{obj.id}.png", "rb"))
        obj.save()


def get_coordinates(interval, step):
    """Функция получения координат для графика"""
    coordinates = tuple()
    return coordinates


def validate_func(func):
    """Функция приводит строковое представление функции, введенное пользователем к валидному виду"""
    math_funcs = ('sqrt', 'tan', 'atan', 'sin', 'asin', 'cos', 'acos')
    func = func.replace('^', '**')
    for f in math_funcs:
        func = func.replace(f, 'math.' + f)
    return func

