import pyodbc

# 3. Создайте соединение и строку подключения.
# ВАЖНО: Замените параметры на свои.
# DRIVER - название драйвера ODBC, установленного в системе (обычно "ODBC Driver 17 for SQL Server" или "SQL Server").
# SERVER - имя вашего сервера (например, localhost, .\SQLEXPRESS).
# DATABASE - имя вашей базы данных.

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=MyTestDB;"
    "UID=sa;"
    "PWD=YourStrongPassword123;"
    "TrustServerCertificate=yes;"
)

try:
    # Устанавливаем соединение
    print("Попытка подключения к MS SQL Server...")
    conn = pyodbc.connect(connection_string)
    
    # 2. Создайте курсор из соединения
    cursor = conn.cursor()
    print("Соединение успешно установлено!")

    # Выполняем SELECT запрос к MS SQL Server
    # Замените 'Users' на имя вашей таблицы
    query = "SELECT Id, Name FROM Users" 
    
    # Выполняем запрос (execute)
    cursor.execute(query)

    # 4. Результат выведите в консоль с помощью цикла for
    print("\nРезультат запроса:")
    print("-" * 30)
    
    # Перебираем строки результата
    for row in cursor:
        # row - это объект Row, к элементам можно обращаться по индексу [0], [1]
        # или по имени колонки, если использовать row.Name
        print(f"ID: {row[0]}, Name: {row[1]}")

    print("-" * 30)

except pyodbc.Error as e:
    print("Ошибка при работе с базой данных:")
    print(e)

finally:
    # Закрываем соединение
    if 'conn' in locals() and conn:
        conn.close()
        print("Соединение закрыто.")