import matplotlib.pyplot as plt

data = [5, 6, 5, 7, 9, 10, 8, 6, 5, 3, 5, 4, 3, 2, 6, 4, 2, 4, 5, 4, 9, 5, 8, 12, 11, 6, 8]

plt.hist(data, bins=3, rwidth=0.9) # создаем гистограмму данных data с 4 интервалами
plt.title('Гистограмма количества часов сна')
plt.xlabel('часы сна')
plt.ylabel('количество людей')

plt.show()