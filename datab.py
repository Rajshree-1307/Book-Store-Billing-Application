import sqlite3

# Function creating the table
def data():
    con=sqlite3.connect("BOOK.db")
    cur=con.cursor()
    cur.execute("Create TABLE IF NOT EXISTS food(b1a text,b2a text,b3a text,b4a text,b5a text,b6a text,b7a text,b8a text,b1b text,b2b text,b3b text,b4b text,b5b text,b6b text,b7b text,b8b text,b1c text,b2c text,b3c text,b4c text,b5c text,b6c text,b7c text,b8c text,tot text)")
    print("Table has been created")
    con.commit()
    con.close()

# Function for inserting values inside the table

def addrec(orderno,fr,br,dr,pz,ct,sb,tax,sr,tot):
    con=sqlite3.connect("BOOK.db")
    cur=con.cursor()
    cur.execute("INSERT INTO books VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(b1a,b2a,b3a,b4a,b5a,b6a,b7a,b8a,b1b,b2b,b3b,b4b,b5b,b6b,b7b,b8b,b1c,b2c,b3c,b4c,b5c,b6c,b7c,b8c,tot))
    print("Record has been successfully added")
    con.commit()
    con.close()
# Funtion for displaying the content of the table

def viewdata():
    con=sqlite3.connect("BOOK.db")
    cur=con.cursor()
    cur.execute("SELECT * from books")
    rows=cur.fetchall()
    con.close()
    return rows

data()