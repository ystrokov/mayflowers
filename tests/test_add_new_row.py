import pytest
from data import SQL_request, Fake
from page_objects.main import BasePage
from conftest import start


@pytest.mark.parametrize("query", [SQL_request.MAIN_REQUEST.value, SQL_request.CASE_VERIFY.value])
def test_add_new_row(start, query):
    base_page = BasePage(start)

    # Отправляем sql запрос добавление новых полей в таблицу
    base_page.entry_sql_query(SQL_request.THIRD_CASE.value)

    # Отправляем sql запрос - "SELECT * FROM Customers;"
    base_page.entry_sql_query(query)
    # Ожидаем, что таблица загрузится
    base_page.waiting_table()

    # Проверяем, что все ранее добавленные данные появились в таблице
    base_page.check_all_occurrences_in_string(str(Fake.company_name), str(Fake.person_name), str(Fake.address),
                                              str(Fake.city), str(Fake.postal_code), str(Fake.country))


'''
Данный кейс можно решить разными способами.
Например в данном случае я выбираю все строки таблицы, исключительно чтобы показать реализацию функции...
check_all_occurrences_in_string, которая проходится по всем элементам двумерного массива и проверяет, что все
6 объектов находятся в строке. Так как тестовое задание нацелено на раскрытие навыков, оставил данный вариант.
Но в бою реализовывал бы более простыми способами.

В реальной ситуации я бы использовал запрос:
SELECT * FROM Customers
ORDER BY CustomerID DESC
LIMIT 1;

P.S Написал параметризованный тест с использованием вышеуказанного запроса

Для того чтобы избежать ситуации, когда цикл проходит по миллиону строк и тем самым усложняет прохождение теста.
Так же данная реализация не подошла бы при пагинации таблицы. (если записей больше чем может быть на странице)


Можно так же проверить по вхождению нового CustomerID, но если эта БД используется кем то еще, то кейс был-бы
нерелевантен.

Можно использовать запрос который я указывал выше и обойтись без цикла. Зная что у нас всего одна строка,
Мы легко можем обратиться к каждому элементу в строке и сделать проверку через assert
'''
