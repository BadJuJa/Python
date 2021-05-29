import sqlite3

# Подключение к БД
con = sqlite3.connect(input())

# Создание курсора
cur = con.cursor()

# Выполнение запроса и получение всех результатов
result = cur.execute("""SELECT title FROM films
                    WHERE (duration >= 60) AND (genre=(SELECT id FROM genres WHERE title = 'комедия'))""").fetchall()

# Вывод результатов на экран
for elem in result:
    print(elem[0])

con.close()