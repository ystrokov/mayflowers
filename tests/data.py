from enum import Enum

from faker import Faker


class Fake:
    fake = Faker()
    company_name = fake.company()
    person_name = fake.name()
    address = fake.address()
    city = fake.city()
    postal_code = fake.postalcode()
    country = fake.country()


class SQL_request(Enum):
    MAIN_REQUEST = 'SELECT * FROM Customers;'

    FIRST_CASE = "SELECT * FROM " \
                 "Customers WHERE ContactName = 'Giovanni Rovelli' " \
                 "AND Address = 'Via Ludovico il Moro 22'; "

    SECOND_CASE = "SELECT * FROM Customers " \
                  "WHERE City = 'London'"

    THIRD_CASE = "INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country) " \
                 f"VALUES ('{Fake.company_name}', '{Fake.person_name}', '{Fake.address}', " \
                 f"'{Fake.city}', '{Fake.postal_code}', '{Fake.country}');"

    CASE_VERIFY = "SELECT * FROM Customers ORDER BY CustomerID DESC LIMIT 1;"

    FOURTH_CASE = f"UPDATE Customers SET CustomerName = '{Fake.company_name}', " \
                  f"ContactName = '{Fake.person_name}', " \
                  f"Address = '{Fake.address}', " \
                  f"City = '{Fake.city}', " \
                  f"PostalCode = '{Fake.postal_code}', " \
                  f"Country = '{Fake.country}' " \
                  "WHERE CustomerID = (SELECT MAX(CustomerID) FROM Customers);"

    FIFTH_CASE = "DELETE FROM Customers WHERE CustomerID = (SELECT MAX(CustomerID) FROM Customers);"

    COUNT_ROWS = "SELECT COUNT(*) AS TotalRows FROM Customers;"
