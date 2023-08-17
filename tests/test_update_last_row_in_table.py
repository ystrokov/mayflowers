import pytest

from enums.data import SQL_request, Fake
from page_objects.main import BasePage


@pytest.mark.usefixtures
@pytest.mark.parametrize("query", [SQL_request.MAIN_REQUEST.value, SQL_request.CASE_VERIFY.value])
def test_update_last_row_in_table(start, query):
    base_page = BasePage(start)
    # Отправляем sql запрос добавление новых полей в таблицу
    base_page.entry_sql_query(SQL_request.FOURTH_CASE.value)
    # Отправляем sql запрос - "SELECT * FROM Customers;"

    base_page.entry_sql_query(query)
    # Ожидаем, что таблица загрузится

    base_page.waiting_table()
    # Проверяем, что все ранее добавленные данные появились в таблице
    base_page.check_all_occurrences_in_string(str(Fake.company_name), str(Fake.person_name), str(Fake.address),
                                              str(Fake.city), str(Fake.postal_code), str(Fake.country))
