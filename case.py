import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

# Настройка веб-драйвера Firefox
options = webdriver.FirefoxOptions()
options.add_argument("--headless")  # Опция для запуска браузера в фоновом режиме (без графического интерфейса)
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)

# Открытие веб-страницы
url = "https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/"
driver.get(url)

# Ожидание загрузки страницы
time.sleep(5)

# Поиск элементов, содержащих цены
prices = driver.find_elements(By.XPATH, '//span[@data-mark="MainPrice"]')

# Парсинг цен и сохранение их в список
price_list = [price.text for price in prices]

# Закрытие веб-драйвера
driver.quit()

# Запись данных в CSV файл
with open('cian_prices.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for price in price_list:
        writer.writerow({'Price': price})

print("Данные успешно сохранены в cian_prices.csv")


# Закрытие веб-драйвера
driver.quit()
