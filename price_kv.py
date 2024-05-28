import csv

# Функция для очистки и преобразования цены
def clean_price(price):
    return int(price.replace(' ₽/мес.', '').replace(' ', ''))

# Чтение данных из CSV файла и обработка цен
input_file = 'cian_prices.csv'
output_file = 'cian_prices_cleaned.csv'

with open(input_file, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    prices = [clean_price(row['Price']) for row in reader]

# Запись очищенных данных в новый CSV файл
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for price in prices:
        writer.writerow({'Price': price})

print(f"Данные успешно обработаны и сохранены в {output_file}")
