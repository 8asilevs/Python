class Road:
    def __init__(self, length, width, density, thickness):
        self._length, self._width = length, width
        self._density, self._thickness = density, thickness

    def raschyot_massy(self):
        massa = self._length * self._width * self._density * self._thickness
        massa /= 1000
        print(f'Масса асфальта для дороги – {massa} тонн')

road_1 = Road(5000, 20, 25, 5)

road_1.raschyot_massy()
