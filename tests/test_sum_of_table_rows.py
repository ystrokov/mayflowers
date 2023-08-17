from enums.data import SQL_request
from page_objects.main import BasePage


def test_sum_of_table_rows(start):
    base_page = BasePage(start)
    expected_row_count = 6

    # Вводим sql запрос в поле ввода
    base_page.entry_sql_query(SQL_request.SECOND_CASE.value)

    # Ожидаем, что таблица загрузится
    base_page.waiting_table()

    # Проверяем, что адрес и имя в таблице на одной сторке и соответствуют ожидаемым
    actual_row_count = base_page.row_count_checker()
    assert actual_row_count == expected_row_count, \
        f"Ожидалось {expected_row_count} строк, найдено {actual_row_count} строк"
