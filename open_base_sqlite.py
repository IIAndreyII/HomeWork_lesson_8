import sqlite3


def bas_sqlite():
    db = sqlite3.connect('base_1.db')
    cur = db.cursor()
    cur.execute("SELECT * FROM guide")

    tab_bas_sqlite = []

    rows = cur.fetchall()
    for row in rows:
        tab_bas_sqlite.append(row)

    cur.close()
    db.close()

    return tab_bas_sqlite

