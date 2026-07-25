from db_connection import DatabaseConnection

db = DatabaseConnection()

products = db.load_table("products")

print(products)

db.close()