# test_distances.py

import pytest
from cities_distances import calculate_distances  

# Словарь координат городов для тестирования
test_sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def test_calculate_distances():
    expected_distances = {
        'Moscow': {
            'Moscow': 0.0,
            'London': 145.60219778561037,
            'Paris': 130.38404810405297,
        },
        'London': {
            'Moscow': 145.60219778561037,
            'London': 0.0,
            'Paris': 42.42640687119285,
        },
        'Paris': {
            'Moscow': 130.38404810405297,
            'London': 42.42640687119285,
            'Paris': 0.0,
        },
    }

    distances = calculate_distances(test_sites)

    # Проверяем, что расстояния совпадают с ожидаемыми
    for city1 in expected_distances:
        for city2 in expected_distances[city1]:
            assert distances[city1][city2] == pytest.approx(expected_distances[city1][city2], rel=1e-9)

if __name__ == "__main__":
    pytest.main()