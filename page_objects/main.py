from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.main_helper import js_code
from enums.selectors import Main_Selectors
from enums.data import SQL_request


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def waiting_table(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Main_Selectors.MAIN_TABLE.value))
        )

    def entry_sql_query(self, sql_query):
        """
        Метод для заполнения поля ввода и нажатия кнопки RUN

        :param sql_query: Принимает SQL запрос
        """
        self.driver.execute_script(js_code(sql_query))
        self.driver.find_element(By.CLASS_NAME, Main_Selectors.RUN_BUTTON.value).click()

    def return_adress_from_table(self) -> str:
        """
        :return: возвращает адрес из первой строки таблицы
        """

        return self.driver.find_element(By.XPATH, Main_Selectors.ADRESS_TABLE.value).text

    def checking_text_in_same_line(self, address: str, name: str):
        """
        Метод подсчета строк в таблице и сравнение с ожидаемым количеством

        :param name: Имя и Фамилия покупателя
        :param address: Ожидаемый адрес конкретного покупателя
        """

        found = False

        rows = self.driver.find_elements(By.XPATH, Main_Selectors.TABLE.value)
        for row in rows:
            cells = row.find_elements(By.XPATH, f"./td[text()='{name}' or text()='{address}']")
            if len(cells) == 2:
                found = True
                break

        if not found:
            print("Не найдены элементы в одной строке.")

    def row_count_checker(self) -> int:
        """
        Метод подсчета строк в таблице

        :return actual_row_count: фактическое количество строк в таблице
        """

        rows = self.driver.find_elements(By.XPATH, Main_Selectors.TABLE.value)

        # Вычитаем 1 дабы не учитывать титульник
        return len(rows) - 1

    def check_all_occurrences_in_string(self, *args):
        """
        Метод для проверки вхождения всех данных в строку

        :param args: ожидается 6 аргументов в соответствии с столбцами таблицы customers
        """
        rows = self.driver.find_elements(By.XPATH, Main_Selectors.TABLE.value)
        try:
            for row in rows:
                # Находим ячейки в текущей строке
                cells = row.find_elements(By.TAG_NAME, "td")

                # Проверяем, что в строке есть как минимум шесть ячеек
                if len(cells) >= 6:
                    elements_found = [cell.text for cell in cells]

                    # Проверяем наличие всех известных элементов в строке таблицы
                    if all(elem in elements_found for elem in args):
                        break  # Выход из цикла после первой найденной строке с нужными элементами

        except Exception as e:
            print("Произошла ошибка:", e)

    def rows_counter(self):
        """
        Метод вывода количества строк в таблице customers

        :return: количество строк в таблице
        """

        self.entry_sql_query(SQL_request.COUNT_ROWS.value)
        self.waiting_table()
        return self.driver.find_element(By.XPATH, Main_Selectors.TABLE_COUNT.value).text
