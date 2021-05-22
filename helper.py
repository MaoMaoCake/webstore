import sqlite3

class EmptyProductRequestError(Exception):
    pass

class DB:
    def __init__(self):
        self.con=sqlite3.connect("webstore.db")
        self.cursor = self.con.cursor()

    def show_products(self,type=None):
        if type is not None:
            if type == "all":
                product_list = self.cursor.execute("SELECT * FROM products")
            else:
                product_list = self.cursor.execute("SELECT * FROM products WHERE type=?",type)
        else:
            raise EmptyProductRequestError

        return product_list