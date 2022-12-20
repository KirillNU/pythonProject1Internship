import numpy as np
import matplotlib.pyplot as plt

# Создание массива размерностью 7х7, заполненного нулями
my_array = np.zeros(shape=(7, 7), dtype=int)

# Проход по всем элементам массива
for i in range(0, my_array.shape[0]):
    for j in range(0, my_array.shape[1]):
        # Заполнение диагоналей массива единицами
        if i == j or i + j == my_array.shape[0] - 1:
            my_array[i, j] = 1
            # Заполнение центра массива единицами
        if i == my_array.shape[0] // 2 or j == my_array.shape[1] // 2:
            my_array[i, j] = 1
plt.imshow(my_array)
plt.show()
