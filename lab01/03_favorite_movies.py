#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

# TODO здесь ваш код

def favorite_movies(str):
    frst_film = str[0:10]
    last_film = str[-15:]
    scnd_film = str[12:25]
    scnd_from_end = str[-22:-17]
    return '{}\n{}\n{}\n{}'.format(frst_film, last_film, scnd_film,scnd_from_end)



print(favorite_movies(my_favorite_movies))
