class ProductCard:
    def __init__(self, name, price, old_price, sale, type_sale, card_weight):
        self.Name = name
        self.price = price
        self.old_price = old_price
        self.sale = sale
        self.type_sale = type_sale
        self.card_weight = card_weight

    def show(self):
        print("Название", self.Name)
        print('Новая цена', self.price)
        print('Старая цена', self.old_price)
        print('Cкидка', self.sale)
        print("Название акции", self.type_sale)
        print('Измерения товара', self.card_weight)
        print('-' * 50)
