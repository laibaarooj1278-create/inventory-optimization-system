import psycopg2
import pandas as pd


class DatabaseConnection:

    def __init__(self):

        self.connection = psycopg2.connect(
            host="localhost",
            port="5432",
            database="inventory_db",
            user="postgres",
            password="laiba127"
        )

        print("✓ Connected to PostgreSQL Successfully")

    def load_table(self, table_name):

        query = f"SELECT * FROM {table_name};"

        dataframe = pd.read_sql(query, self.connection)

        return dataframe

    def close(self):

        self.connection.close()

        print("✓ Database Connection Closed")