from dataclasses import dataclass

@dataclass
class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    # def __init__(self, name, price, description, quantity):
    #    self.name = name
    #    self.price = price
    #    self.description = description
    #    self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        return self.quantity >= quantity


    def buy(self, quantity):
        if self.check_quantity(quantity):
            self.quantity = self.quantity - quantity
        else:
            raise ValueError("Недостаточно продуктов")
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        if product in self.products.keys():
            self.products[product] = self.products[product] + buy_count
        else:
            self.products[product] = buy_count
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """

    def remove_product(self, product: Product, remove_count=None):
        if remove_count is None or remove_count >= self.products[product]:
            del self.products[product]
        else:
            self.products[product] = self.products[product] - remove_count
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        total_price = 0
        for product in self.products.keys():
            total_price += self.products[product] * product.price
        return total_price

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        for product in self.products.keys():
            if product.check_quantity(self.products[product]):
                product.buy(self.products[product])
            else:
                raise ValueError
        self.clear()