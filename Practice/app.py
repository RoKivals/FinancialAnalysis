from matplotlib.patches import RegularPolygon
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import random
import math
import itertools as itr
import copy


def visualization(cor1: int, cor2: int, *n_array: list):
    # Создаем фигуру и оси
    fig, ax = plt.subplots()

    # Задаем пределы осей
    ax.set_xlim(cor1, cor2)
    ax.set_ylim(cor1, cor2)

    # Рисуем оси координат
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')

    # Рисуем фигуры
    for polygons in n_array:
        for polygon in polygons:
            if len(polygon) <= 2:
                ax.add_patch(RegularPolygon(polygon, numVertices=6, radius=1, facecolor="blue", edgecolor="black"))
            else:
                x = [p[0] for p in polygon]
                y = [p[1] for p in polygon]
                ax.fill(x, y, 'b')

    # Создаем шаг основной сетки
    ax.xaxis.set_major_locator(MultipleLocator(base=2))
    ax.yaxis.set_major_locator(MultipleLocator(base=2))

    # Создаем шаг вторичной сетки
    ax.xaxis.set_minor_locator(MultipleLocator(base=1))
    ax.yaxis.set_minor_locator(MultipleLocator(base=1))

    # Создаем основную и вторичную сетки
    ax.grid(which='minor')
    ax.grid(which='major', lw=1.5)
    ax.set_aspect('equal')
    plt.show()


def gen_rectangle(count, negative=1):
    array, array_neg = [], []
    n = 0
    for i in range(count):
        array.append([[i + n, 0], [i + n, 2], [i + 1 + n, 2], [i + 1 + n, 0]])
        if negative:
            array_neg.append([[-i - n - 1, 0], [-i - n - 1, 2], [-i - 2 - n, 2], [-i - 2 - n, 0]])
        n += 1
    return array + array_neg


def gen_triangle(count, negative=1):
    array, array_neg = [], []
    n = 0
    for i in range(count):
        array.append([[i + n, 0], [(i + 1 + n), 2], [i + 2 + n, 0]])
        if negative:
            array_neg.append([[-i - n - 1, 0], [(-i - 2 - n), 2], [-i - 3 - n, 0]])
        n += 2
    return array + array_neg


def gen_hexagon(count, negative=1):
    array, array_neg = [], []
    n = 0
    for i in range(count):
        array.append([i + n + 1, 1])
        if negative:
            array_neg.append([-i - n - 2, 1])
        n += 2
    return array + array_neg


def generate_figures():
    rectangles = gen_rectangle(3, negative=0)
    triangles = gen_triangle(2, negative=0)
    hexagons = gen_hexagon(2, negative=0)
    for i in range(3):
        for j in range(4):
            rectangles[i][j][0] = rectangles[i][j][0] + 5 * i
    for i in range(2):
        for j in range(3):
            triangles[i][j][0] = triangles[i][j][0] + 2 + 5 * i
    for i in range(2):
        hexagons[i][0] = hexagons[i][0] + 4 + 5 * i

    figures = list(itr.chain(rectangles, triangles, hexagons))
    return figures


def tr_translate(array: list, x=0, y=4):
    new_array = copy.deepcopy(array)

    for arr in new_array:
        if len(arr) > 2:
            for i in arr:
                i[0] += x
                i[1] += y

        elif len(arr) <= 2:
            arr[0] += x
            arr[1] += y

    return new_array


def tr_rotate(array: list, offset=2):
    new_array = copy.deepcopy(array)
    array = new_array[:int(len(new_array) / 2)]
    array_neg = new_array[int(len(new_array) / 2):]
    print(array)
    n = 0
    for arr1 in array:
        if len(arr1) > 2:
            for i in arr1:
                if offset >= 0:
                    i[1] += n
                elif offset < 0:
                    i[1] += n - offset

        elif len(arr1) <= 2:
            if offset >= 0:
                arr1[1] += n
            elif offset < 0:
                arr1[1] += n - offset
        n += offset
    print(array)
    if offset < 0:
        n = offset * 2
    else:
        n = 0
    for arr2 in array_neg:
        if len(arr2) > 2:
            for i in arr2:
                if offset >= 0:
                    i[1] += -n - offset
                elif offset < 0:
                    i[1] -= n

        elif len(arr2) <= 2:
            if offset >= 0:
                arr2[1] += -n - offset
            elif offset < 0:
                arr2[1] -= n
        n += offset

    return array + array_neg


def tr_symmetry(array: list, center_of_symmetry=2):
    new_array = copy.deepcopy(array)  # Модуль copy для глубокого копирования

    for arr in new_array:
        if len(arr) > 3:
            for i in arr:
                i[1] += center_of_symmetry

        elif len(arr) == 3:
            just_value = [2, -2, 2]
            for num, i in enumerate(arr):
                i[1] += center_of_symmetry + just_value[num]

        elif len(arr) <= 2:
            arr[1] += center_of_symmetry

    return new_array


def tr_homothety(array: list, corner=0, index=0):
    new_array = copy.deepcopy(array)
    array = new_array[:int(len(new_array) / 2)]
    array_neg = new_array[int(len(new_array) / 2):]

    n = 0
    k = 0
    for arr1 in array:

        if len(arr1) > 3:
            rn_lst = [0, 0, k, k]
            for num, i in enumerate(arr1):
                if corner >= 0:
                    i[1] += n
                elif corner < 0:
                    i[1] += n - 2
                i[0] += rn_lst[num]

        elif len(arr1) == 3:
            rn_lst = [0, n, n + n]
            for num, i in enumerate(arr1):
                if corner >= 0:
                    i[1] += n
                elif corner < 0:
                    i[1] += n - 2
                i[0] += rn_lst[num]

        n += corner
        k += index

    n = 0
    k = 0
    for arr2 in array_neg:

        if len(arr2) > 3:
            rn_lst = [0, 0, -k, -k]
            for num, i in enumerate(arr2):
                if corner >= 0:
                    i[1] += -n - 2
                elif corner < 0:
                    i[1] += -n
                i[0] += rn_lst[num]

        elif len(arr2) == 3:
            rn_lst = [0, -n, -n - n]
            for num, i in enumerate(arr2):
                if corner >= 0:
                    i[1] += -n - 2
                elif corner < 0:
                    i[1] += -n

                i[0] += rn_lst[num]

        n += corner
        k += index

    return array + array_neg

visualization(-15, 15, gen_rectangle(10))
visualization(-15, 15, gen_triangle(10))
visualization(-15, 15, gen_hexagon(10))
visualization(0, 30, generate_figures())
visualization(-15, 15,tr_translate(gen_rectangle(10), y=5))
visualization(-15, 15, tr_rotate(gen_rectangle(10), 2))
visualization(-15, 15, tr_symmetry(gen_triangle(10), 2), gen_triangle(10))
visualization(-15, 15, tr_homothety(gen_rectangle(10), 3, 2))
visualization(-15, 15, tr_rotate(tr_translate(gen_rectangle(10), y=3), 1), tr_rotate(gen_rectangle(10), 1),\
             tr_rotate(tr_translate(gen_rectangle(10), y=-3), 1))
visualization(-15, 15, tr_rotate(tr_translate(gen_rectangle(10), y=4), -1), tr_rotate(gen_rectangle(10), 1))
visualization(-15, 15, tr_symmetry(gen_triangle(10), 3), gen_triangle(10))
visualization(-15, 15, tr_homothety(gen_rectangle(10), 2, 1))
