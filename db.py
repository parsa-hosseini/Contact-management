import sqlite3

class Database:
    
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute( """
                            CREATE TABLE IF NOT EXISTS Contacts (id INTEGER PRIMARY KEY,
                            name text, family text, address text, phone text)
                            """)
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM Contacts")
        rows = self.cur.fetchall()
        return rows
   
    
    def insert(self, name, family, address, phone):
       
        self.cur.execute("""
                            INSERT INTO Contacts VALUES( NULL, ?, ?, ?, ?)
                            """, (name, family, address, phone))
        self.con.commit()
        
        print(self.cur.rowcount, "Record Inserted!")
        print("Last ID is: ", self.cur.lastrowid)
        

    def remove(self, id):
        self.cur.execute("DELETE FROM Contacts WHERE id = ?", (id,))
        self.con.commit()

    def update(self, id, name, family, address, phone):
        self.cur.execute("""
                            UPDATE Contacts SET name = ?, family = ?, address = ? , phone = ? WHERE id = ?
                            """ , (name, family, address, phone, id))
        self.con.commit()

    def search_id(self, id):
        # print("Last ID is: ", self.cur.lastrowid)
        # print(id , self.cur.lastrowid)
        # if id <= lastrow:
        #     self.cur.execute("SELECT  * FROM Contacts WHERE id = ?", (id,) )
        #     row = self.cur.fetchone()
        #     return row
        # else:
        #     return 0
       
        self.cur.execute("SELECT  * FROM Contacts WHERE id = ?", (id,) )
        row = self.cur.fetchone()
        return  row       
 
    def search_name(self , name):
           self.cur.execute("SELECT  * FROM Contacts WHERE name = ?", (name,))
           row = self.cur.fetchone()
           return row
    def search_family(self , family):
        self.cur.execute("SELECT  * FROM Contacts WHERE family = ?", (family,))
        row = self.cur.fetchone()
        return row

    def search_phone(self , phone):
        self.cur.execute("SELECT  * FROM Contacts WHERE phone = ?", (phone,))
        row = self.cur.fetchone()
        return row
    
    def __del__(self):
        self.con.close()




# d = Database('C:/Users/ParsaHosseini/Documents/m/x.db')
# d.insert('parsa', 'asd', 'address', '123')
# d.insert('name', 'family', 'address', '3252345')
# a = d.search_id(1)
# print(a)
# print(a[2])
# a = d.search_phone('123')
# print(a)


        
