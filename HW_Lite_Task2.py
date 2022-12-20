import numpy as np

pointD = (4, 3)  # Задание координат точки в декартовой системе координат
x = pointD[0]  # Сохраняем координату x
y = pointD[1]  # Сохраняем координату y
r = np.sqrt(x ** 2 + y ** 2)  # Расчет полярного радиуса
a = np.arctan(y / x)  # Расчет полярного угла (в качестве)
pointP = (r, a)
print("Координаты точки в декартовой системе: ", pointD)
print("Координаты точки в полярной системе:   ", pointP)
