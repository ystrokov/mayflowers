from enums.data import SQL_request
from page_objects.main import BasePage


def test_delete_last_row_from_table(start):
    base_page = BasePage(start)
    # подсчет первоначального количества строк
    before_rows_counter = base_page.rows_counter()
    base_page.waiting_table()

    # Вводим sql запрос в поле ввода
    base_page.entry_sql_query(SQL_request.FIFTH_CASE.value)

    # Повторно считаем строки
    after_rows_counter = base_page.rows_counter()

    # Ожидаем, что таблица загрузится
    base_page.waiting_table()

    # Проверяем, что количество строк в таблице уменьшилось
    assert before_rows_counter > after_rows_counter, f"Первоначальное количество строк ({before_rows_counter} строк) " \
                                                     f"больше или равно текущему ({after_rows_counter} строк)"
