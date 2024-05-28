import numpy as np
import matplotlib.pyplot as plt

# a = np. zeros((3,3), dtype = int) # матрица из нулей размером 3x3
# a = np.ones((2,5)) # матрица из 1 размером 2x5
# a = np.random.random((4, 5)) # случайная матрица размером 4x5
# a = np.arange(0, 10, 2) # рядовое разбиение от 0 до 10 с шагом 2 (от 0 до 10 включительно)
# a = np.linspace(0, 13, 10) # равномерное разбиение от 0 до 13 в 10 частей
# print(a)

x = np.linspace(-10, 10, 100)
y = x**2

plt.plot(x, y)
plt.xlabel('ось x')
plt.ylabel('ось y')
plt.title('График y = x^2')
plt.grid(True, which='both', linestyle='--', color='gray', linewidth=0.5)
plt.show()