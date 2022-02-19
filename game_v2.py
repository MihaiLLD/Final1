"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        
        if number == predict_number:
            break  # выход из цикла если угадали
    return count
    
def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

def best_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count=0
    min_border=1 #начальная нижняя граница 
    max_border=100 #начальная верхняя граница 
    koef=0.55  #коэффициент дробления участка
   
    while True:
        count+=1
        limit_border=max_border-min_border #определение размера участка исследования
        #смещение верхней и нижней границ участка к загадочному числу
        if min_border+round(limit_border*koef)>number:  
            max_border=min_border+round(limit_border*koef)
            if max_border-round(limit_border*koef)<number:
                min_border=max_border-round(limit_border*koef)
        else:
            min_border=max_border-round(limit_border*koef)
            if  min_border+round(limit_border*koef)>number:
                max_border=min_border+round(limit_border*koef)

        #выход из цикла , когда одна из границ находит загадочное число
        if min_border==number or max_border==number:
         break

    return count

def score_game2(best_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        best_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    
    for number in random_array:
        count_ls.append(best_predict(number))
       
    score = int(np.mean(count_ls))
    
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

if __name__ == "__main__":
    # RUN
    score_game(random_predict)
    score_game2(best_predict)


