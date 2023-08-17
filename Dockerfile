# Используйте базовый образ, который содержит Selenium, Chrome и WebDriver
FROM joyzoursky/python-chromedriver:3.8

# Создайте рабочую директорию
# Создайте рабочую директорию
WORKDIR /mayflowers

# Установите git и копируйте исходные файлы проекта
RUN apt-get update && apt-get install -y git && \
    git clone https://github.com/ystrokov/mayflowers.git . && \
    ls

# Установите зависимости из requirements.txt
RUN pip3 install -r requirements.txt

# Запустите тесты
CMD ["pytest"]
