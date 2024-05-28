import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_samples = 100  # Количество образцов
x = np.random.rand(num_samples)  # Массив из num_samples случайных чисел
y = np.random.rand(num_samples)  # Другой массив из num_samples случайных чисел

# Построение диаграммы рассеяния
plt.scatter(x, y, c='blue', alpha=0.5)

# Добавление заголовка и меток осей
plt.title('Диаграмма рассеяния для случайных данных')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True, linestyle='-', alpha=0.5, linewidth=0.75)

# Показать график
plt.show()
