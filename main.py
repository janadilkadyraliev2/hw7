from db import create_database
from product import add_products, update_quantity, update_price, delete_product
from product import fetch_all_products, fetch_products_by_price_and_quantity, search_products_by_title

if __name__ == "__main__":
    create_database()  # Создание базы данных и таблицы
    add_products()  # Добавление 15 различных товаров

    print("Все товары:")
    fetch_all_products()  # Выбор и печать всех товаров

    print("\nОбновляем количество товара с id = 1 на 50:")
    update_quantity(1, 50)

    print("\nОбновляем цену товара с id = 2 на 25.50:")
    update_price(2, 25.50)

    print("\nВсе товары после обновлений:")
    fetch_all_products()

    print("\nУдаляем товар с id = 3:")
    delete_product(3)

    print("\nВсе товары после удаления:")
    fetch_all_products()

    print("\nТовары с ценой меньше 100 и количеством больше 5:")
    fetch_products_by_price_and_quantity(100, 5)

    print("\nПоиск товаров по названию 'Товар':")
    search_products_by_title("Товар")
