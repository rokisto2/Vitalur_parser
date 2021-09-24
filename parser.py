from bs4 import BeautifulSoup

import product_card

ans = []

with open("index.html", 'r') as f:
    file = f.read()
soup = BeautifulSoup(file, 'lxml')
products = soup.find_all('a', class_="card")
Product = product_card.ProductCard
for product in products:
    card_action= product.find('div', class_="card-top__left").find('div', class_="card-action").get_text(strip=True)
    c = product.find('div', class_="card-price-sm").find('span', class_='card-price-sm__old')
    if str(card_action) != "1+1" and str(card_action) != "Дивные цены" and c is not None:
        ans.append(Product(
            product.find('div', class_="card__title").get_text(strip=True),
            float(product.find('div', class_="card-price-lg").find('span').get_text(strip=True)) + float(int(product.find('div', class_="card-price-sm").find('span', class_='card-price-sm__new').get_text(strip=True)))/ 100,
            float(product.find('div', class_="card-price-sm").find('span', class_='card-price-sm__old').get_text(strip=True)),
            product.find('div', class_="card-top__left").find('div', class_="card-action__discount").get_text(
                strip=True),
            product.find('div', class_="card-top__left").find('div', class_="card-action").get_text(strip=True),
            product.find('div', class_="card-top__right").find('div', class_='card-weight').get_text(strip=True),
        ))

    elif card_action == '1+1':
        ans.append(Product(
            product.find('div', class_="card__title").get_text(strip=True),
            float(product.find('div', class_="card-price-lg").find('span').get_text(strip=True)) + float(
                int(product.find('div', class_="card-price-sm").find('span', class_='card-price-sm__new').get_text(
                    strip=True))) / 100,
            (float(product.find('div', class_="card-price-lg").find('span').get_text(strip=True)) + float(
                int(product.find('div', class_="card-price-sm").find('span', class_='card-price-sm__new').get_text(
                    strip=True))) / 100)*2,
            '50%',
            product.find('div', class_="card-top__left").find('div', class_="card-action").get_text(strip=True),
            product.find('div', class_="card-top__right").find('div', class_='card-weight').get_text(strip=True),
        ))
    else:
        ans.append(Product(
            product.find('div', class_="card__title").get_text(strip=True),
            float(product.find('div', class_="card-price-lg").find('span').get_text(strip=True)) + float(
                int(product.find('div', class_="card-price-sm").find('span', class_='card-price-sm__new').get_text(
                    strip=True))) / 100,
            float(product.find('div', class_="card-price-lg").find('span').get_text(strip=True)) + float(
                int(product.find('div', class_="card-price-sm").find('span', class_='card-price-sm__new').get_text(
                    strip=True))) / 100,
            '0%',
            product.find('div', class_="card-top__left").find('div', class_="card-action").get_text(strip=True),
            product.find('div', class_="card-top__right").find('div', class_='card-weight').get_text(strip=True),
        ))
for i in ans:
    print(i.show())