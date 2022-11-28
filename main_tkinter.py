from tkinter import *
from tkinter import ttk
from open_base_sqlite import bas_sqlite
from add_record import add_rec
from del_record import del_rec
from search_record import search_rec



def main_tk():

    def click(event):
        add_rec()
        root.destroy()
        # main_tk()

    def click2(event):
        del_rec()()

    def click3(event):
        search_rec()

    def click4(event):
        root.destroy()

    def click5(event):
        root.destroy()
        main_tk()



    root = Tk()
    root.title('Сотрудники.')
    root.minsize(width=1100, height=600)

    but = Button(root, text='Добавить запись', font="Arial 10",
                    width=20, height=2, bg='white', fg='blue',bd=5)

    but1 = Button(root, text='Удалить запись', font="Arial 10",
                width=20, height=2, bg='white', fg='blue',bd=5)

    but2 = Button(root, text='Поиск', font="Arial 10",
                width=20, height=2, bg='white', fg='blue',bd=5)

    but3 = Button(root, text='Выход', font="Arial 10",
                width=20, height=2, bg='white', fg='blue',bd=5)

    but4 = Button(root, text='Обновить таблицу', font="Arial 10",
                width=20, height=2, bg='white', fg='blue',bd=5)




    people = bas_sqlite()

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

    lab = Label(root, text='')
    lab1 = Label(root, text='')

    but.grid(row=0, column=0)
    but1.grid(row=1, column=0)
    but2.grid(row=0, column=3)
    but3.grid(row=1, column=3)
    but4.grid(row=6, column=1)


    lab.grid(row=5, column=0)
    lab1.grid(row=3, column=0)

    tree.grid(row=4, column=1)




    but.bind("<Button-1>", click)
    but1.bind("<Button-1>", click2)
    but2.bind("<Button-1>", click3)
    but3.bind("<Button-1>", click4)
    but4.bind("<Button-1>", click5)


    root.mainloop()


