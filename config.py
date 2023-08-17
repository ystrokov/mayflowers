import os

DRIVER_URL = os.environ.get('URL', 'https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all')
WEBDRIVER_URL = os.environ.get('WEBDRIVER_URL', 'http://selenium:4444/wd/hub')
LOCALHOST = os.environ.get('LOCALHOST', 'http://localhost:4444/wd/hub')

capabilities = {"browserName": "chrome",
                "browserVersion": "114.0",
                "platformName": "linux",
                "pageLoadStrategy": "none"}
