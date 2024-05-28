import matplotlib.pyplot as plt

x = [2, 6, 8, 14, 20]
y = [6, 4, 10, 12, 16]

plt.scatter(x, y) # строим точечную диаграмму рассеивания
plt.title('Тестовая диаграмма рассеивания')
plt.xlabel('Ось x')
plt.ylabel('Ось y')

plt.show()