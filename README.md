# mayflowers

Тестовый проект в компанию mayflowers

## Установка

* Cкачать **[docker-compose.yml](https://github.com/ystrokov/mayflowers/blob/main/docker-compose.yml "docker-compose.yml")** 
* В терминале перейти в папку с файлом
* Выполнить команду:
> docker compose up -d

После чего должна начаться сборка образов и запуск контейнеров.

### selenium
> образ отвечает за запуск **seleniarm/standalone-chromium**
> по URL localhost:4444 можно перейти в UI интерфейс для использования веб-визора  
### testrunner
> образ **joyzoursky/python-chromedriver** необходим для запуска автотестов на стороне python. Соединен внутренней сетью с контейнером **selenium** 

## Реализация
в файле **[test_add_new_row.py](https://github.com/ystrokov/mayflowers/blob/main/tests/test_add_new_row.py"test_add_new_row.py")** есть небольшое пояснение по реализации. Если кратко, то решил отказаться от избыточных проверок, дабы не делать паровоз внутри каждого теста. Вместо этого реализовал методы проверки конкретных рейсов.

P.S Шаг с ожиданием страницы так же можно было вынести, но все предыдущие реализации ломались об него. Решил по итогу оставить, чтобы в тесте было чуть больше двух строк :)
