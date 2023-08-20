"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def second_product():
    return Product("postcard", 50, "This is a postcard", 50)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1000)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(100)
        assert product.quantity == 900

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1100)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product_to_cart(self, cart, product):
        cart.add_product(product, 3)

        assert cart.products[product] == 3

    def test_remove_product_from_cart_more_than_available(self, cart, product):
        cart.add_product(product, 3)
        cart.remove_product(product, 10)

        assert cart.products == {}

    def test_remove_product_from_cart_if_not_remove_count(self, cart, product):
        cart.add_product(product, 3)
        cart.remove_product(product)

        assert cart.products == {}

    def test_remove_product_from_cart(self, cart, product):
        cart.add_product(product, 5)
        cart.remove_product(product, 3)

        assert cart.products[product] == 2

    def test_clear_cart(self, cart, product, second_product):
        cart.add_product(product, 5)
        cart.add_product(second_product, 5)
        cart.clear()

        assert cart.products == {}

    def test_get_total_price(self, cart, product, second_product):
        cart.add_product(product, 10)
        cart.add_product(second_product, 3)

        assert cart.get_total_price() == 1150

    def test_buy_more_products_that_available(self, cart, product):
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            cart.buy()

    def test_buy_products(self, cart, product):
        cart.add_product(product, 10)
        cart.buy()

        assert product.quantity == 990