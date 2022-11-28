from tkinter import *
import sqlite3



def add_rec():

    def clickles(event):

        res = ent_tab_num.get()
        res1 = ent_surname.get()
        res2 = ent_post.get()
        res3 = ent_structure.get()
        res4 = ent_phone.get()
        res5 = ent_age.get()

        db = sqlite3.connect('base_1.db')
        cur = db.cursor()
        res8 = [(res, res1,res2,res3,res4,res5)]
        print(res8)

        cur.executemany("INSERT INTO guide VALUES(?, ?, ?, ?, ?, ?)", res8)

        db.commit()
        cur.close()
        db.close()
        
        root.destroy()

        
        
        
    



                
    root = Tk()
    root.title('Добавить запись')
    root.minsize(width=550, height=250)

    lbl_tab_num = Label(root, text='Введите Табельный номер', width=30)
    lbl_surname = Label(root, text='Введите Фамилию', width=30)
    lbl_post = Label(root, text='Введите должность', width=30)
    lbl_structure = Label(root, text='Введите категорию', width=30)
    lbl_phone = Label(root, text='Введите телефон', width=30)
    lbl_age = Label(root, text='Введите возраст', width=30)


    ent_tab_num = Entry(root, width=30, font="Arial 12", state='normal', bd=5)
    ent_surname = Entry(root, width=30, font="Arial 12", state='normal', bd=5)
    ent_post = Entry(root, width=30, font="Arial 12", state='normal', bd=5)
    ent_structure = Entry(root, width=30, font="Arial 12", state='normal', bd=5)
    ent_phone = Entry(root, width=30, font="Arial 12", state='normal', bd=5)
    ent_age = Entry(root, width=30, font="Arial 12", state='normal', bd=5)




    but = Button(root, text='Добавить запись',
                width=20, height=2, bg='white', fg='blue',bd=3)


    lbl_tab_num.grid(row=0, column=0)
    lbl_surname.grid(row=1, column=0)
    lbl_post.grid(row=2, column=0)
    lbl_structure.grid(row=3, column=0)
    lbl_phone.grid(row=4, column=0)
    lbl_age.grid(row=5, column=0)

    ent_tab_num.grid(row=0, column=1)
    ent_surname.grid(row=1, column=1)
    ent_post.grid(row=2, column=1)
    ent_structure.grid(row=3, column=1)
    ent_phone.grid(row=4, column=1)
    ent_age.grid(row=5, column=1)



    but.grid(row=6, column=1)


    but.bind("<Button-1>", clickles)

    root.mainloop()



