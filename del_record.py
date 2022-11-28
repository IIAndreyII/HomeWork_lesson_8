from tkinter import *
import sqlite3

def del_rec():
    def clickles1(event):
        
        res = ent_tab_num.get()
        res1 = ''
        res1 = (res1 + res)
        print(type(res1))
        print(res1)

        db = sqlite3.connect('base_1.db')
        cur = db.cursor()
        cur.execute("DELETE FROM guide WHERE tab_num = ?",(res1,))


        db.commit()
        cur.close()
        db.close()

        root.destroy()


    root = Tk()
    root.title('Удалить запись')
    root.minsize(width=550, height=250)

    lbl_tab_num = Label(root, text='Введите табельный номер', width=30)

    ent_tab_num = Entry(root, width=30, font="Arial 12", state='normal', bd=5)

    but = Button(root, text='Удалить',
                    width=20, height=2, bg='white', fg='blue',bd=3)

    lbl_tab_num.grid(row=0, column=0)

    ent_tab_num.grid(row=0, column=1)

    but.grid(row=1, column=1)


    but.bind("<Button-1>", clickles1)

    root.mainloop()



