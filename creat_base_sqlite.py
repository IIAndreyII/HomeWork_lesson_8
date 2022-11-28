import sqlite3

db = sqlite3.connect('base_1.db')

c = db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS guide(
    tab_num text,
    surname text,
    post text,
    structure text,
    phone text,
    age integer
)""")

c.execute("INSERT INTO guide (tab_num, surname, post, structure, phone, age) VALUES('345', 'Сергеев', 'Директор', 'Руководитель', '+7(903)123-45-67', 45)")
c.execute("INSERT INTO guide (tab_num, surname, post, structure, phone, age) VALUES('276', 'Иванов', 'Зам.директора', 'Руководитель', '+7(921)654-87-42', 34)")
c.execute("INSERT INTO guide (tab_num, surname, post, structure, phone, age) VALUES('478', 'Петров', 'Гл.инженер', 'Руководитель', '+7(987)345-56-19', 37)")
c.execute("INSERT INTO guide (tab_num, surname, post, structure, phone, age) VALUES('456',  'Глазова', 'Инженер', 'Специалист', '+7(435)543-26-19', 28)")
c.execute("INSERT INTO guide (tab_num, surname, post, structure, phone, age) VALUES('348', 'Громова', 'Бухгалтер', 'Специалист', '+7(803)321-54-67', 47)")
c.execute("INSERT INTO guide (tab_num, surname, post, structure, phone, age) VALUES('470', 'Глазова', 'Сборщик', 'Рабочий', '+7(876)345-76-19', 42)")
c.execute("INSERT INTO guide (tab_num, surname, post, structure, phone, age) VALUES('356', 'Пушкин', 'Сварщик', 'Рабочий', '+7(999)123-32-56', 56)")
c.execute("INSERT INTO guide (tab_num, surname, post, structure, phone, age) VALUES('473', 'Фёдоров', 'Водитель', 'Рабочий', '+7(234)546-83-67', 27)")


db.commit()


c.close()
db.close()