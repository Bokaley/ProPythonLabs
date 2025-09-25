#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

# TODO здесь заполнение словаря
def calculate_distances(sites_data):
    distances = {}
    cities = list(sites_data.keys())

    for i in range(len(cities)):
        for j in range(i, len(cities)):
            city1 = cities[i]
            city2 = cities[j]

            x1, y1 = sites_data[city1]
            x2, y2 = sites_data[city2]

            dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

            if city1 == city2:
                dist = 0.0

            if city1 not in distances:
                distances[city1] = {}
            if city2 not in distances:
                distances[city2] = {}

            distances[city1][city2] = dist
            distances[city2][city1] = dist
    return distances

distances = calculate_distances(sites)

print(distances)






