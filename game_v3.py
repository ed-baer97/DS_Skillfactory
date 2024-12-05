import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Функция угадывает загаданное число за минимальное количество попыток.
    Разбивает список чисел на 2 промежутка и от середины проверяет.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    low = 1
    high = 100
    predict = (low + high) // 2  # Начальное предположение (середина диапазона)

    while predict != number:
        count += 1
        if predict < number:
            low = predict + 1  # Число больше предположения, сужаем диапазон снизу
        elif predict > number:
            high = predict - 1  # Число меньше предположения, сужаем диапазон сверху
        predict = (low + high) // 2  # Обновляем предположение

    return count


    
    
        
