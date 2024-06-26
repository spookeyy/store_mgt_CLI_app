# category module

from lib.config import DATABASE, CURSOR

class Category:

# creating a new category
    @classmethod
    def create_a_category(cls, name, store_id):
        sql = "INSERT INTO category (name, store_id) VALUES (?, ?)"
        CURSOR.execute(sql, (name, store_id))
        DATABASE.commit()

    @classmethod
    def add_category(cls, name, store_id):
        sql = "INSERT INTO category (name, store_id) VALUES (?, ?)"
        CURSOR.execute(sql, (name, store_id))
        DATABASE.commit()
        category_id = CURSOR.lastrowid
        CURSOR.execute("SELECT * FROM category WHERE id = ?", (category_id,))
        return CURSOR.fetchone()

# updating an existing category
    @classmethod
    def update_category_by_id(cls, id, name):
        sql = "UPDATE category SET name = ? WHERE id = ?"
        CURSOR.execute(sql, (name, id))
        DATABASE.commit()
# getting categories
    @classmethod
    def get_all_categories(cls):
        sql = "SELECT * FROM category"
        CURSOR.execute(sql)
        return CURSOR.fetchall()

    @classmethod
    def get_categories_by_store_id(cls, store_id):
        sql = "SELECT * FROM category WHERE store_id = ?"
        CURSOR.execute(sql, (store_id,))
        return CURSOR.fetchall()

    @classmethod
    def get_category_by_id(cls, id):
        sql = "SELECT * FROM category WHERE id = ?"
        CURSOR.execute(sql, (id,))
        return CURSOR.fetchone()

    @classmethod
    def get_category_by_name(cls, name):
        sql = "SELECT * FROM category WHERE name = ?"
        CURSOR.execute(sql, (name,))
        return CURSOR.fetchone()

    @classmethod
    def get_category_by_product_id(cls, product_id):
        sql = "SELECT * FROM category WHERE product_id = ?"
        CURSOR.execute(sql, (product_id,))
        return CURSOR.fetchall()

# deleting categories
    @classmethod
    def delete_category_by_id(cls, id):
        sql = "DELETE FROM category WHERE id = ?"
        CURSOR.execute(sql, (id,))
        DATABASE.commit()

    @classmethod
    def delete_category_by_name(cls, name):
        sql = "DELETE FROM category WHERE name = ?"
        CURSOR.execute(sql, (name,))
        DATABASE.commit()

    @classmethod
    def delete_all_categories_in_store(cls, store_id):
        sql = "DELETE FROM category WHERE store_id = ?"
        CURSOR.execute(sql, (store_id,))
        DATABASE.commit()

    @classmethod
    def delete_all_categories(cls):
        sql = "DELETE FROM category"
        CURSOR.execute(sql)
        DATABASE.commit()

    # @classmethod
    # def delete_category_by_product_id(cls, product_id):
    #     sql = "DELETE FROM category WHERE product_id = ?"
    #     CURSOR.execute(sql, (product_id,))
    #     DATABASE.commit()

    # @classmethod
    # def delete_category_by_store_id(cls, store_id):
    #     sql = "DELETE FROM category WHERE store_id = ?"
    #     CURSOR.execute(sql, (store_id,))
    #     DATABASE.commit()

# # creating 5 sample categories
# category1 = Category.add_category("Grocery", 1)
# category2 = Category.add_category("Fruits", 1)
# category3 = Category.add_category("Vegetables", 1)
# category4 = Category.add_category("Meat", 1)
# category5 = Category.add_category("Dairy", 1)