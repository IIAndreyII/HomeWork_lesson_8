from tkinter import *
from tkinter import ttk
import sqlite3

def search_rec():


    def click11(event):


        res1 = str(ent_surname.get())

        db = sqlite3.connect('base_1.db')
        cur = db.cursor()

        cur.execute("SELECT * FROM guide WHERE surname = ?", (res1,))
        people = (cur.fetchall())

        db.commit()
        cur.close()
        db.close()

        columns = ("tab_num","surname", "post", "structure", "phone", "age")

        tree = ttk.Treeview(columns=columns, show="headings")

        tree.heading("tab_num", text="Табельный номер")
        tree.heading("surname", text="Фамилия")
        tree.heading("post", text="Должность")
        tree.heading("structure", text="Категория")
        tree.heading("phone", text="Телефон")
        tree.heading("age", text="Возраст")

        for person in people:
            tree.insert("", END, values=person)

        tree.grid(row=4, column=1)
        # Делал таблицу в этом окне но она стала копироваться в таблицу
        # main_tkinter.py почему не понял. Сделал закрытие окна.
        root.destroy()



    root = Tk()
    root.title('Поиск')
    root.minsize(width=550, height=250)



    lbl_surname = Label(root, text='Введите: Фамилию', width=30)
    ent_surname = Entry(root, width=30, font="Arial 12", state='normal', bd=5)
    lbl_surname.grid(row=0, column=0)
    ent_surname.grid(row=0, column=1)

    but = Button(root, text='Ввести', font="Arial 10",
                width=10, height=1, bg='white', fg='blue',bd=3)
    but.bind("<Button-1>", click11)
    but.grid(row=1, column=1)


    root.mainloop()


