from sqlite3 import Connection

class Pais:
    """ Tabla id name"""
    def create_table(self,conn:Connection):
        query = """
            CREATE TABLE IF NOT EXISTS PAIS (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50) NOT NULL
            );
            """
        cursor=conn.cursor()
        cursor.execute(query)
        conn.commit()
        