from .models import Category

def bmiCounter(height, weight):
    bmi = weight / height**2

    if 19 < bmi < 25:
        return ['Диеты для спортсменов', 'Средиземноморская диета']
    elif bmi <= 19:
        return ['Палео-диета', 'Кето-диета (кетогенная диета)']
    elif bmi >= 25:
        return ['Диета для снижения веса', 'Средиземноморская диета', 'Сыроедение (Ро-питание)', 'Вегетарианство']