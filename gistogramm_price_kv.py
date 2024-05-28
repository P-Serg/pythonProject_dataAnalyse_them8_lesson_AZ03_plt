import csv
import matplotlib.pyplot as plt

# Чтение данных из CSV файла
prices = []

with open('cian_prices_cleaned.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        prices.append(int(row['Price']))

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(prices, bins=20, edgecolor='black')
plt.title('Распределение цен на квартиры')
plt.xlabel('Цена (руб)')
plt.ylabel('Количество')

# Отображение гистограммы
plt.grid(True)
plt.show()
