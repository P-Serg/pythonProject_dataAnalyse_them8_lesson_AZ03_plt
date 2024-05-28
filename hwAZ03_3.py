import csv
import time
import statistics
from selenium import webdriver
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt

driver = webdriver.Firefox()

# Открытие сайта
driver.get('https://www.divan.ru/perm/category/divany-i-kresla')

prices = []

time.sleep(2)  # Задержка для загрузки страницы
items = driver.find_elements(By.CSS_SELECTOR, 'span[class="ui-LD-ZU KIkOH"]')
for item in items:
    price_text = item.text.replace('руб.', '').replace(' ', '').strip()
    if price_text.isdigit():
        prices.append(int(price_text))

driver.quit()

# Запись данных в CSV файл
with open('prices.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Price'])
    for price in prices:
        writer.writerow([price])

# Вычисление средней цены
if prices:
    average_price = statistics.mean(prices)
    print(f'Средняя цена: {average_price} рублей')
else:
    print("Не удалось собрать данные о ценах.")

# Построение гистограммы цен
if prices:
    plt.hist(prices, bins=20, edgecolor='black')
    plt.title('Гистограмма цен на диваны')
    plt.xlabel('Цена (руб)')
    plt.ylabel('Количество')
    plt.grid(True)
    plt.show()
else:
    print("Нет данных для построения гистограммы.")
