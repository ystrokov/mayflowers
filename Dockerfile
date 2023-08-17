# Используйте базовый образ, который содержит Selenium, Chrome и WebDriver
FROM joyzoursky/python-chromedriver:3.8

# Создайте рабочую директорию
WORKDIR /app

# Копируйте исходные файлы проекта
COPY . /app

# Установите зависимости Python
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt

# Запустите тесты
CMD ["pytest"]
