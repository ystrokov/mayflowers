from enums.data import SQL_request
from page_objects.main import BasePage
import pytest


@pytest.mark.parametrize("query", [SQL_request.MAIN_REQUEST.value, SQL_request.FIRST_CASE.value])
def test_verify_name_and_address_for_customer(start, query):
    base_page = BasePage(start)
    # Отправляем sql запрос
    base_page.entry_sql_query(query)

    # Ожидаем, что таблица загрузится
    base_page.waiting_table()

    # Проверяем, что адрес и имя в таблице на одной сторке и соответствуют ожидаемым
    base_page.checking_text_in_same_line("Via Ludovico il Moro 22", "Giovanni Rovelli")