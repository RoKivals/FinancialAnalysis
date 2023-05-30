import numpy


class MapParams(object):
    def __init__(self, data: numpy.array, width: int = 650, height: int = 450):
        # Точки движения тайфуна
        self.dots = data

        self.zoom: int = 3  # Масштаб карты на старте. Изменяется от 1 до 17
        self.type: str = "map"  # Другие значения "sat", "sat,skl"

        # Разрешение изображения (максимум 650x450)
        if 0 < width <= 650:
            self.width: int = width
        else:
            raise ValueError("Максимальная ширина: 650")
        if 0 < height <= 450:
            self.height: int = height
        else:
            raise ValueError("Максимальная высота: 450")

    # Размеры выходного изображения
    def size_key(self):
        return str(self.width) + "," + str(self.height)

    def bbox_key(self):
        borders = self.find_borders()
        result = f'{borders[0][1]:.1f},{borders[0][0]:.1f}~{borders[1][1]:.1f},{borders[1][0]:.1f}'
        return result

    def find_borders(self):
        max_coord = list(numpy.amax(self.dots, axis=0))
        min_coord = list(numpy.amin(self.dots, axis=0))
        return min_coord, max_coord

    def line_key(self):
        result = ''
        for i in self.dots:
            result += f'{i[1]:.2f},{i[0]:.2f},'
        return result[:-1]
